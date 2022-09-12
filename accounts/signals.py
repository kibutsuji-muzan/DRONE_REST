from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from django.contrib.auth import user_logged_in, user_logged_out

from accounts.models.userOtp import VerificationDevice
from accounts.models.userModel import User #, LoggedInUser
from accounts.models.profileModel import UserProfile, ProfileImage
from core import settings

from post_office import mail
from sms import send_sms

Send_Mail = Signal()
Send_Sms = Signal()

@receiver(Send_Mail)
def SendMail(sender, data, **kwargs):
    maildata = data.get('mail')
    context = data.get('context')
    mail.send([sender.email,], settings.EMAIL_HOST_USER, subject=maildata.subject, message=maildata.content, html_message=maildata.html_content, context=context, priority='now')


@receiver(Send_Sms)
def SendSms(sender, data, **kwargs):
    send_sms(data.get('message'), settings.DEFAULT_FROM_SMS, [str(sender.phone),], fail_silently=False, priority='now')


@receiver(post_save, sender=User)
def createOtp(sender, instance, created, **kwargs):
    if created:
        VerificationDevice.objects.get_or_create(unverified_phone=(instance.email if instance.email else str(instance.phone)), user = instance)


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        if instance.email:
            UserProfile.objects.create(email = instance.email, user = instance)
        else:
            UserProfile.objects.create(phone = instance.phone, user = instance)


@receiver(post_save, sender=UserProfile)
def createProfileImage(sender, instance, created, **kwargs):
    if created:
        ProfileImage.objects.create(profile=instance)


# @receiver(user_logged_in)
# def on_user_logged_in(sender, request, **kwargs):
#     LoggedInUser.objects.get_or_create(user=kwargs.get('user')) 


# @receiver(user_logged_out)
# def on_user_logged_out(sender, **kwargs):
#     LoggedInUser.objects.filter(user=kwargs.get('user')).delete()