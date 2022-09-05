from django.db import models
from accounts.models.userModel import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class ProfileType(models.Model):
    id = models.UUIDField(_("UUID"), primary_key=True, editable=False, unique=True, default=uuid.uuid4)

    name= models.CharField(_("Name"),max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Type")
        verbose_name_plural = _("User Types")

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    GENDER = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]

    id = models.UUIDField(_("UUID"), primary_key=True, editable=False, unique=True, default=uuid.uuid4)

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))

    first_name = models.CharField(_('First Name'), max_length=20)
    last_name = models.CharField(_('Last Name'), max_length=20)
    email = models.EmailField(_('Email'), max_length=200, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    birthday = models.DateField(_('Birth Date'),blank=True,null=True)
    gender = models.CharField(_('Gender'), max_length=6, choices=GENDER,blank=True,null=True)

    def __str__(self):
        return self.email if self.email else str(self.phone)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")
        

class ProfileImage(models.Model):
    id = models.UUIDField(_("UUID"), primary_key=True, editable=False, unique=True, default=uuid.uuid4)

    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name=_("Profile"), related_name='profile_image')

    image = models.ImageField(_("Image"), upload_to="ProfileImages/", default="ProfileImages/default.png")
    alt_txt = models.CharField(_("Alternative Text"), max_length=20, default="Your Profile Image")
    created_at = models.DateTimeField(_("Created On"),auto_now=True,editable=False)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    
    class Meta:
        verbose_name = _("Profile Image")
        verbose_name_plural = _("Profile Images")

class ProfileUpdateRequest(models.Model):
    
    id = models.UUIDField(_("UUID"), primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    
    user = models.OneToOneField(UserProfile, verbose_name=_("User"), on_delete=models.CASCADE)
    changeRequest = models.ForeignKey(ProfileType, verbose_name=_("Change Request"), on_delete=models.CASCADE)

    is_verified = models.BooleanField(_("Is Verified"), default=False)

    def __str__(self):
        return self.user.email

    class Meta:
        managed = True
        verbose_name = _("Profile Update Request")
