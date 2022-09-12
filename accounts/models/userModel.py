from time import strftime
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.manager import UserManager
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class UserType(models.Model):
    id = models.UUIDField(_("UUID"), primary_key=True, editable=False, unique=True, default=uuid.uuid4)

    name= models.CharField(_("Name"),max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Type")
        verbose_name_plural = _("User Types")

    def __str__(self):
        return self.name


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

    user_type = models.ManyToManyField(UserType, verbose_name=_("User Types"), through="UserUpdateRequest", through_fields=('user', 'updateto'))

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email if self.email else str(self.phone)
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

def expiryTime():
    hour = str(int(strftime('%H')) + 1)
    return hour + strftime(':%M:%S')


class UserUpdateRequest(models.Model):

    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    updateto = models.ForeignKey(UserType, verbose_name=_("Update Request"), on_delete=models.CASCADE)

    desc = models.TextField(_("Description"))

    is_verified = models.BooleanField(_("Is Verified"), default=False)

    def __str__(self):
        return self.user.email

    class Meta:
        managed = True
        verbose_name = _("User Update Request")


class PassResetToken(models.Model):

    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='reset_token')

    token = models.UUIDField(_("Token-Key"), default = uuid.uuid4)

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

