from django_otp.models import Device
from django.db import models
from django_otp.util import hex_validator, random_hex
from django_otp.oath import TOTP
from time import time
from binascii import unhexlify
import logging
from django.utils.translation import gettext_lazy as _
from accounts.models.userModel import User


def default_key():
    return random_hex(20)

#django_otp Device model to generate and verify token.
class VerificationDevice(Device):
    unverified_phone = models.SlugField(_("Unverified Phone"),max_length=255,unique=True)
    secret_key = models.CharField(
        _("Secret Key"),
        max_length=40,
        default=default_key,
        validators=[hex_validator],
        help_text="Hex-encoded secret key to generate totp tokens.",
        unique=True,
    )
    last_verified_counter = models.BigIntegerField(
        _("Last Verified Counter"),
        default=-1,
        help_text=("The counter value of the latest verified token."
                   "The next token must be at a higher counter value."
                   "It makes sure a token is used only once.")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    step = models.IntegerField(default=300)
    digits = models.IntegerField(default=6)


    class Meta(Device.Meta):
        verbose_name = "Verification Device"

    @property
    def bin_key(self):
        return unhexlify(self.secret_key.encode())

    def totp_obj(self):
        totp = TOTP(key=self.bin_key, step=self.step, digits=self.digits)
        time.time()
        # totp.time = time()
        return totp

    def generate_challenge(self):
        totp = self.totp_obj()
        token = str(totp.token()).zfill(self.digits)

        message = _("Your token for Cadasta is {token_value}."
                   " It is valid for {time_validity} minutes.")
        message = message.format(
        token_value=token, time_validity=self.step // 60)

        logging.debug("Token has been sent to %s " % self.unverified_phone)
        logging.debug("%s" % message)
        return token


    def verify_token(self, token, tolerance=0):
        totp = self.totp_obj()
        try:
            token = int(token)
        except ValueError:
            self.verified = False
        if ((totp.t() > self.last_verified_counter) and
                (totp.verify(token, tolerance=tolerance))):
            self.last_verified_counter = totp.t()
            self.verified = True
            self.save()
        else:
            self.verified = False
        return self.verified