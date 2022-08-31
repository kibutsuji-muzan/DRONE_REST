from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models.profileModel import UserProfile
from droneshop.models.product import Product
from droneservice.models.service import Service
import uuid

class ContactUs(models.Model):

    name = models.CharField(_("Name"), max_length=30)
    email = models.EmailField(_("Email"), blank=True, null=True)
    phone = PhoneNumberField()

    created_at = models.DateTimeField(auto_now=True,editable=False)
    
    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _("Contact Us")

class Review(models.Model):

    user = models.ForeignKey(UserProfile, verbose_name=_("Review From"), on_delete=models.CASCADE)

    review = models.TextField(_("Review"), max_length=300)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    
    def __str__(self):
        return self.user.email

    class Meta:
        managed = True
        verbose_name = _("Review")

class Reports(models.Model):
    title = models.CharField(_("Title"), max_length=30)
    desc = models.CharField(_("Description"), max_length=300)

    user = models.ForeignKey(UserProfile, verbose_name = _("Report By"), on_delete=models.CASCADE)

    product = models.ForeignKey(Product, verbose_name = _("On Product"), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    class Meta:
        app_label = 'droneshop'
        managed = True
        verbose_name = _("Report")

class Complaints(models.Model):

    title = models.CharField(_("Title"), max_length=30)
    desc = models.CharField(_("Description"), max_length=300)

    user = models.ForeignKey(UserProfile, verbose_name = _("Report By"), on_delete=models.CASCADE)

    service = models.ForeignKey(Service, verbose_name= _("On Service"), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    class Meta:
        app_label = 'droneservice'
        managed = True
        verbose_name = _("Complaint")