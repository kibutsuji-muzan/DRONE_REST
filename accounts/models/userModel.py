from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

from accounts.manager import UserManager

from phonenumber_field.modelfields import PhoneNumberField
from upload_validator import FileTypeValidator
from time import strftime
import uuid

from django_otp.util import hex_validator, random_hex


validator = FileTypeValidator(
    allowed_types=['application/msword'],
    allowed_extensions=['.doc', '.docx']
)

def default_key():
    return random_hex(40)

def expiryTime():
    hour = str(int(strftime('%H')) + 1)
    return hour + strftime(':%M:%S')



class User(AbstractUser):

    GENDER = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]
    username = None
    first_name = None
    last_name = None

    id = models.UUIDField(_('UUID'),default=uuid.uuid4,null=False , primary_key=True, editable=False)

    email = models.EmailField(_("Email"), max_length=254, null=True, blank=True, unique=True)
    phone = PhoneNumberField(_("Phone Number"), blank=True, null=True)

    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email if self.email else str(self.phone)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class ShopOrganizationType(models.Model):

    Choices = [
    ('manufacturer','Manufacturer'),
    ('seller','Seller'),
    ('distributor', 'Distributor'),
    ('assembler', 'Assembler')
    ]

    type= models.CharField(_("Type"),max_length=30, choices=Choices, unique=True, primary_key=True, editable=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Organization Type")
        verbose_name_plural = _("Organization Types")

    def __str__(self):
        return self.type


class UpdateRequest(models.Model):#Rename it to something better

    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='update_request')
    org = models.ForeignKey(ShopOrganizationType, verbose_name=_("Update Request"), on_delete=models.CASCADE, related_name='uodate_to')

    desc = models.TextField(_("Description"))
    organization_name = models.CharField(_("Organization Name"), max_length=200, blank=True, null=True)
    phone = PhoneNumberField(_("Phone Number"), blank=True, null=True)

    is_verified = models.BooleanField(_("Is Verified"), default=False)

    def __str__(self):
        return self.user.email

    class Meta:
        managed = True
        verbose_name = _("User Upgrade Resquest")


class UserUpdateFiles(models.Model):

    file_of = models.ForeignKey(UpdateRequest, on_delete=models.CASCADE, related_name='request_file')

    image = models.ImageField(_("Image"), upload_to="ProfileImages/", default="ProfileImages/download.jpeg", validators=[FileTypeValidator(allowed_types=[ 'image/*'])])

    def __str__(self):
        return self.file_of


class PassResetToken(models.Model):

    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='reset_token')

    token = models.CharField(_("Token-Key"), max_length=41, default=default_key, validators=[hex_validator],)

    expiry = models.TimeField(_("Expiry"), auto_now=False, auto_now_add=False, default=expiryTime)
    created_at = models.TimeField(_("Ceated At"), auto_now_add=True)

    def __str__(self):
        return self.token


# class LoggedInUser(models.Model):
#     user = models.OneToOneField(RadixUser,verbose_name=_("User") ,related_name='logged_in_user', on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=32, null=True, blank=True,verbose_name=_("Session Key"))
#     user_agent = models.SlugField(max_length=255,null=True, blank=True,verbose_name=_("User Agent"))
#     client_ip = models.SlugField(max_length=255,null=True, blank=True,verbose_name=_("Client IP"))

#     def __str__(self):
#         return self.user.email
#     class Meta:
#         verbose_name = _("Logged In User")
#         verbose_name_plural = _("Logged In Users")
#         model_lable = _("LoggedInUser")

