from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Category(MPTTModel):

    name = models.CharField(_('Name'), max_length=20, blank=True)
    parent = TreeForeignKey('self', verbose_name=_('Parent'), related_name='children',on_delete=models.CASCADE, null=True, blank=True, )
    slug = models.SlugField(_("URL"), max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category", args={self.slug})
    def __str__(self):
        return self.name

class CategoryByUser(models.Model):

    name = models.CharField(_('Name'), max_length=20, blank=True)
    slug = models.SlugField(_("URL"), max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Category By User")
        verbose_name_plural = _("Categories By User")

    def get_absolute_url(self):
        return reverse("store:category", args={self.slug})

    def __str__(self):
        return self.name