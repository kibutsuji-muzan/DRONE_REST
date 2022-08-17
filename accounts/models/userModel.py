import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.manager import UserManager
from django.utils import timezone
from accounts.models.usertypeModel import UserType

class User(AbstractUser):

    GENDER = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]
    username = None
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    first_name = models.CharField(_("First Name"),max_length=30, blank=True)
    last_name = models.CharField(_("Last Name"),max_length=30, blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=12, unique=False, blank=True)
    gender = models.CharField(_('Gender'),choices=GENDER, max_length=6, blank=True)
    birthday = models.DateField(_('Birth Date'), default=timezone.now, blank=True)
    user_uuid = models.UUIDField(_('UUID'),default=uuid.uuid4,primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    #have to create another model for user type this one is category not type edit this one
    usertype = models.ForeignKey(UserType, verbose_name=_('User Type'), blank=True, on_delete=models.DO_NOTHING,null=True)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# class LoggedInUser(models.Model):
#     user = models.OneToOneField(RadixUser,verbose_name=_("User") ,related_name='logged_in_user', on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=32, null=True, blank=True,verbose_name=_("Session Key"))
#     user_agent = models.SlugField(max_length=255,null=True, blank=True,verbose_name=_("User Agent"))
#     client_ip = models.SlugField(max_length=255,null=True, blank=True,verbose_name=_("Client IP"))

#     def __str__(self):
#         return self.user.email