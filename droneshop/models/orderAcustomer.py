from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from droneshop.models.product import Product
from accounts.models.profileModel import UserProfile

class customer(models.Model):

    customerId = models.UUIDField(_("Customer Id"), default = uuid.uuid4, blank=True, primary_key=True)

    customer = models.ForeignKey(UserProfile, verbose_name=_("User"), on_delete=models.CASCADE)

    class META:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")
        
    def __str__(self):
        return self.customer.name

class orderedItem(models.Model):

    orderId = models.UUIDField(_("Order Id"), default=uuid.uuid4, primary_key=True)

    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    customerId = models.ForeignKey(customer, verbose_name=_("Customer"), on_delete=models.CASCADE, null=True)
    class META:
        verbose_name = _("Ordered Item")
        verbose_name_plural = _("Ordered Items")

    def __str__(self):
        return self.product.name

