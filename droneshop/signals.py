from django.dispatch import receiver, Signal
from django.db.models.signals import post_save

from droneshop.models.product import ProductVerificationRequest, Product


@receiver(post_save,sender=Product)
def create_request(sender, instance, created, **kwargs):
    ProductVerificationRequest.objects.create(product_name=instance)
