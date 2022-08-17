from django.db import models
from drone_api.models.category import Category
from django.utils.translation import gettext_lazy as _

class ServiceType(models.Model):
    name = models.CharField(_("Name"), max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _("Service Type")
        verbose_name_plural = _("Service Types")

    def __str__(self):
        return self.name


class Service(models.Model):

    ServiceType = models.ForeignKey(ServiceType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(_("Name"),max_length=20)
    title = models.CharField(_("Title"), max_length=255)
    desc = models.CharField(_("Description"), max_length=255)
    slug = models.SlugField(_("URL"), max_length=50)
    price = models.DecimalField(_("Service Price"),max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name

class ServiceDetail(models.Model):
    name = models.CharField(_("Name"),max_length=255)
    ServiceType = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Service Detail")
        verbose_name_plural = _("Service Details")

    def __str__(self):
        return self.name


class ServiceDetailValue(models.Model):
    Service = models.ForeignKey(Service,on_delete=models.CASCADE)
    Detail = models.ForeignKey(ServiceDetail, on_delete=models.RESTRICT)
    value = models.CharField(_("Value"), max_length=50)

    class Meta:
        verbose_name = _("Service Detail Value")
        verbose_name_plural = _("Service Detail Values")

    def __str__(self):
        return self.value