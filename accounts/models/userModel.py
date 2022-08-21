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

    user_uuid = models.UUIDField(_('UUID'),default=uuid.uuid4,primary_key=True,editable=False)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    phone_number = PhoneNumberField()
    gender = models.CharField(_('Gender'),choices=GENDER, max_length=6, blank=True)
    birthday = models.DateField(_('Birth Date'), default=timezone.now, blank=True)

    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
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
#         
