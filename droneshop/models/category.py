from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from accounts.models.profileModel import UserProfile

class Category(models.Model):

    name = models.CharField(_('Name'), max_length=20, blank=True)
    slug = models.SlugField(_("URL"), max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

class CategoryByUser(models.Model):

    createdBy = models.ForeignKey(UserProfile,verbose_name=_("Created By"),on_delete=models.CASCADE)

    name = models.CharField(_('Name'), max_length=20, blank=True)
    slug = models.SlugField(_("URL"), max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Category By User")
        verbose_name_plural = _("Categories By User")

    def __str__(self):
        return self.name