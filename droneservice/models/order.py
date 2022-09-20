from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from droneservice.models.service import Service
from accounts.models.profileModel import UserProfile

class customer(models.Model):
    
    uuid = models.UUIDField(_("PID"), max_length=20, unique=True, editable=False, primary_key=True, default=uuid.uuid4)

    user = models.ForeignKey(UserProfile, verbose_name=_("User"), on_delete=models.CASCADE, related_name='service_customer')

    address = models.CharField(_("Address"), max_length=50)

    is_active = models.BooleanField(default=True)

    class META:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")
        
    def __str__(self):
        return self.user.email

class orderedService(models.Model):

    STATUS = [('pending','Pending'),('shipping','Shipping'),('dilivered','Dilivered')]

    uuid = models.UUIDField(_("Order Id"), default=uuid.uuid4, editable=False,primary_key=True)

    service = models.ForeignKey(Service, verbose_name=_("Product"), on_delete=models.CASCADE)
    customerId = models.ForeignKey(customer, verbose_name=_("Customer"), on_delete=models.CASCADE, null=True)

    status = models.CharField(choices=STATUS, max_length=9, default='pending')
    address = models.CharField(_("Address"), max_length=50, blank=True, null=True)

    class META:
        verbose_name = _("Ordered Item")
        verbose_name_plural = _("Ordered Items")

    def __str__(self):
        return self.servece.name


