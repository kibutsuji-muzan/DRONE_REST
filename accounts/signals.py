from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models.userOtp import VerificationDevice
from accounts.models.userModel import User#, LoggedInUser
from accounts.models.profileModel import UserProfile
# from django.contrib.auth import user_logged_in, user_logged_out


@receiver(post_save, sender=User)
def createOtp(sender, instance, created, **kwargs):
    if created:
        VerificationDevice.objects.get_or_create(unverified_phone=(instance.email if instance.email else str(instance.phone)), user = instance)

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if instance.email:
        UserProfile.objects.get_or_create(email = instance.email , birthday = instance.birthday, gender = instance.gender,user = instance)
    else:
        UserProfile.objects.get_or_create(phone = instance.phone , birthday = instance.birthday, gender = instance.gender,user = instance)

# @receiver(user_logged_in)
# def on_user_logged_in(sender, request, **kwargs):
#     LoggedInUser.objects.get_or_create(user=kwargs.get('user')) 


# @receiver(user_logged_out)
# def on_user_logged_out(sender, **kwargs):
#     LoggedInUser.objects.filter(user=kwargs.get('user')).delete()