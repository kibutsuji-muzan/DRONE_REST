import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.manager import UserManager
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):

    GENDER = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]
    username = None
    first_name = None
    last_name = None

    id = models.UUIDField(_('UUID'),default=uuid.uuid4,null=False , primary_key=True, editable=False)

    email = models.EmailField(_("Email"), max_length=254, null=True, blank=True, unique=True)
    phone = PhoneNumberField(_('Phone Number'), blank=True, null=True)
    gender = models.CharField(_('Gender'),choices=GENDER, max_length=6, blank=True,null=True)
    birthday = models.DateField(_('Birth Date'), blank=True,null=True)

    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email if self.email else str(self.phone)
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")



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

