from statistics import mode
from django.db import models
from droneshop.models.category import Category, CategoryByUser
from django.utils.translation import gettext_lazy as _
from accounts.models.profileModel import UserProfile
import uuid

class Product(models.Model):
    uuid = models.UUIDField(_("UUID"), primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    owner = models.ForeignKey(UserProfile, verbose_name=_('Owner'), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT,related_name="Product")
    categoryByUser = models.ForeignKey(CategoryByUser, verbose_name=_('Category By Owner'), on_delete=models.SET_NULL, null=True, related_name="Product_User")

    name = models.CharField(_("Name"),max_length=20)
    title = models.CharField(_("Title"), max_length=255)
    desc = models.CharField(_("Description"), max_length=255)
    slug = models.SlugField(_("URL"), max_length=50)
    price = models.DecimalField(_("Product Price"),max_digits=7, decimal_places=2)
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

    Product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_detail')

    detail_key = models.CharField(_("Detail"), max_length=50, null=True)
    value_key = models.CharField(_("Value"), max_length=50)

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

    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name.name

    class Meta:
        verbose_name = _("Product Verification")
        verbose_name_plural = _("Products Verification")