from django.db import models
from accounts.models.userModel import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from mptt.models import MPTTModel, TreeForeignKey

class ProfileType(MPTTModel):

    parent = TreeForeignKey('self', verbose_name=_('Parent'),on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name= models.CharField(_("Name"),max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = _("User Type")
        verbose_name_plural = _("User Types")

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    GENDER = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"), primary_key=True)
    userType = models.ForeignKey(ProfileType ,verbose_name=_('Type Of User'), null=True, on_delete=models.SET_NULL)

    first_name = models.CharField(_('First Name'), max_length=20)
    last_name = models.CharField(_('Last Name'), max_length=20)
    email = models.EmailField(_('Email'), max_length=200, unique=True)
    phone = PhoneNumberField()
    birthday = models.DateField(_('Birth Date'))
    gender = models.CharField(_('Gender'), max_length=6, choices=GENDER)

    def __str__(self):
        full_name = self.first_name + self.last_name
        return full_name
    
    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")
        

class ProfileImage(models.Model):

    image = models.ImageField(_("Image"), upload_to="ProfileImages/", default="ProfileImages/default.png")
    alt_txt = models.CharField(_("Alternative Text"), max_length=20, default="Your Profile Image")
    created_at = models.DateTimeField(_("Created On"),auto_now=True,editable=False)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name=_("Profile"))
    class Meta:
        verbose_name = _("Profile Image")
        verbose_name_plural = _("Profile Images")
