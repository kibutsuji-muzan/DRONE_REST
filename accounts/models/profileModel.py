from django.db import models
from accounts.models.userModel import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from upload_validator import FileTypeValidator


class UserProfile(models.Model):
    GENDER = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, editable=True, unique=True, verbose_name=_("User"), related_name='user_profile')

    first_name = models.CharField(_('First Name'), max_length=20, blank=True, null=True)
    last_name = models.CharField(_('Last Name'), max_length=20, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=200, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    gender = models.CharField(_('Gender'),choices=GENDER, max_length=6, blank=True, null=True)
    birthday = models.DateField(_('Birth Date'), blank=True, null=True)

    def __str__(self):
        return self.email if self.email else str(self.phone)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")
        

class ProfileImage(models.Model):

    profile = models.OneToOneField(UserProfile, primary_key=True, on_delete=models.CASCADE, verbose_name=_("Profile"), related_name='profile_image',)

    image = models.ImageField(_("Image"), upload_to="ProfileImages/", default="ProfileImages/download.jpeg", validators=[FileTypeValidator(allowed_types=[ 'image/*'])])
    alt_txt = models.CharField(_("Alternative Text"), max_length=20, default="Your Profile Image")
    created_at = models.DateTimeField(_("Created On"),auto_now=True,editable=False)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    
    class Meta:
        verbose_name = _("Profile Image")
        verbose_name_plural = _("Profile Images")
