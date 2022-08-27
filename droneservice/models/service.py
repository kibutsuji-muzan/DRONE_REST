from statistics import mode
from django.db import models
from droneservice.models.category import Category, CategoryByUser
from django.utils.translation import gettext_lazy as _
from accounts.models.profileModel import UserProfile
import uuid

class Service(models.Model):

    owner = models.ForeignKey(UserProfile, verbose_name=_('Owner'), on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    categoryByUser = models.ForeignKey(CategoryByUser, verbose_name=_('Category By Owner'), on_delete=models.SET_NULL, null=True)

    service_uuid = models.UUIDField(_("Service UUID"), default=uuid.uuid4,primary_key=True,editable=True)
    name = models.CharField(_("Name"),max_length=20)
    title = models.CharField(_("Title"), max_length=255)
    desc = models.CharField(_("Description"), max_length=255)
    slug = models.SlugField(_("URL"), max_length=50)
    price = models.DecimalField(_("Service Price"),max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name

class ServiceDetailValue(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE, related_name='Service_detail')

    detail_key = models.CharField(_("Detail"), max_length=50, null=True)
    value_key = models.CharField(_("Value"), max_length=50)

    class Meta:
        verbose_name = _("Service Detail Value")
        verbose_name_plural = _("Service Detail Values")



class ServiceImage(models.Model):

    service = models.ForeignKey(Service, verbose_name=_("Service"), on_delete=models.CASCADE,related_name="Service_image")

    image = models.ImageField(_("Image"), upload_to="ServiceImages/")
    alt_text = models.CharField(_("Alternative Text"), max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Service Image")
        verbose_name_plural = _("Service Images") 

class ServiceVerificationRequest(models.Model):

    serviceName = models.OneToOneField(Service, verbose_name=_("Service Name"), on_delete=models.CASCADE)

    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.serviceName)
    class Meta:
        verbose_name = _("Service Verification")
        verbose_name_plural = _("Services Verification")