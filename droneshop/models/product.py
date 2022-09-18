from django.db import models
from droneshop.models.category import Category
from django.utils.translation import gettext_lazy as _
from accounts.models.profileModel import UserProfile
import uuid

class Product(models.Model):
    uuid = models.UUIDField(_("UUID"), primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    owner = models.ForeignKey(UserProfile, verbose_name=_('Owner'), on_delete=models.CASCADE, blank=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT,related_name="Product", blank=False, null=True)

    name = models.CharField(_("Name"),max_length=20, blank=False, null=True)
    title = models.CharField(_("Title"), max_length=255, blank=False, null=True)
    desc = models.CharField(_("Description"), max_length=255, blank=False, null=True)
    slug = models.SlugField(_("URL"), max_length=50, blank=False, null=True)
    price = models.DecimalField(_("Product Price"),max_digits=7, decimal_places=2, blank=False, null=True)

    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

class ProductDetailValue(models.Model):
    uuid = models.UUIDField(_("UUID"), primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_detail')

    detail_key = models.CharField(_("Detail"), max_length=50, blank=False, null=True)
    value_key = models.CharField(_("Value"), max_length=50, blank=False, null=True)

    class Meta:
        verbose_name = _("Product Detail Value")
        verbose_name_plural = _("Product Detail & Values")


class ProductImage(models.Model):
    uuid = models.UUIDField(_("UUID"), primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE,related_name="product_image")

    image = models.ImageField(_("Image"), upload_to="ProductImages/")
    alt_text = models.CharField(_("Alternative Text"), max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images") 

class ProductVerificationRequest(models.Model):

    uuid = models.UUIDField(_("UUID"), primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    product_name = models.OneToOneField(Product, verbose_name=_("Product Name"), on_delete=models.CASCADE, related_name="Product")

    def __str__(self):
        return self.product_name.uuid

    class Meta:
        verbose_name = _("Product Verification")
        verbose_name_plural = _("Products Verification")