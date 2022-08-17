from django.db import models
from drone_api.models.category import Category, CategoryByUser
from django.utils.translation import gettext_lazy as _
from accounts.models.userModel import User

class ProductType(models.Model):
    name = models.CharField(_("Name"), max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class Product(models.Model):

    productType = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    owner = models.ForeignKey(User, verbose_name=_('Owner'), on_delete=models.CASCADE, null=True) #remove null later
    categoryForUser = models.ForeignKey(CategoryByUser, verbose_name=_('Category By Owner'), on_delete=models.SET_NULL, null=True)
    name = models.CharField(_("Name"),max_length=20)
    title = models.CharField(_("Title"), max_length=255)
    desc = models.CharField(_("Description"), max_length=255)
    slug = models.SlugField(_("URL"), max_length=50)
    price = models.DecimalField(_("Product Price"),max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
    name = models.CharField(_("Name"),max_length=255)
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Product Detail")
        verbose_name_plural = _("Product Details")

    def __str__(self):
        return self.name


class ProductDetailValue(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Detail = models.ForeignKey(ProductDetail, on_delete=models.RESTRICT)
    value = models.CharField(_("Value"), max_length=50)

    class Meta:
        verbose_name = _("Product Detail Value")
        verbose_name_plural = _("Product Detail Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product_image")
    image = models.ImageField(_("Image"), upload_to="ProductImages/",default="ProductImages/default.png")
    alt_text = models.CharField(_("Alternative Text"), max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")