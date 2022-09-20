from django.dispatch import receiver, Signal
from django.db.models.signals import post_save

from droneservice.models.service import ServiceVerificationRequest, Service


@receiver(post_save,sender=Service)
def create_request(sender, instance, created, **kwargs):
    if created:
        ServiceVerificationRequest.objects.create(service_name=instance)
