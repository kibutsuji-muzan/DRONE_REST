from django.db import models
from droneservice.models.category import Category
from django.utils.translation import gettext_lazy as _

from accounts.models.profileModel import UserProfile
from accounts.models.userModel import User

import uuid
from phonenumber_field.modelfields import PhoneNumberField
from upload_validator import FileTypeValidator



class Service(models.Model):
    uuid = models.UUIDField(_("PID"), max_length=20, unique=True, editable=False, primary_key=True, default=uuid.uuid4)

    owner = models.ForeignKey(UserProfile, verbose_name=_('Owner'), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT,related_name="Product")

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
    uuid = models.UUIDField(_("PID"), max_length=20, unique=True, editable=False, primary_key=True, default=uuid.uuid4)

    service = models.ForeignKey(Service,on_delete=models.CASCADE, related_name='Service_detail')

    detail_key = models.CharField(_("Detail"), max_length=50)
    value_key = models.CharField(_("Value"), max_length=50)

    class Meta:
        verbose_name = _("Service Detail Value")
        verbose_name_plural = _("Service Detail Values")



class ServiceImage(models.Model):
    uuid = models.UUIDField(_("PID"), max_length=20, unique=True, editable=False, primary_key=True, default=uuid.uuid4)

    service = models.ForeignKey(Service, verbose_name=_("Service"), on_delete=models.CASCADE,related_name="Service_image")

    image = models.ImageField(_("Image"), upload_to="ServiceImages/")
    alt_text = models.CharField(_("Alternative Text"), max_length=255, blank=True, default='service image')
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Service Image")
        verbose_name_plural = _("Service Images") 


class ServiceVerificationRequest(models.Model):
    uuid = models.UUIDField(_("UUID"), primary_key=True, default=uuid.uuid4, editable=False)

    service_name = models.OneToOneField(Service, verbose_name=_("Service Name"), on_delete=models.CASCADE)

    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.service_name)

    class Meta:
        verbose_name = _("Service Verification")
        verbose_name_plural = _("Services Verification")



# class ServiceType(models.Model):

#     Choices = [
#     ('manufacturer','Manufacturer'),
#     ('seller','Seller'),
#     ('distributor', 'Distributor'),
#     ('assembler', 'Assembler')
#     ]

#     type= models.CharField(_("Type"),max_length=30, choices=Choices, unique=True, primary_key=True, editable=True)
#     created_at = models.DateTimeField(auto_now=True,editable=False)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = _("Organization Type")
#         verbose_name_plural = _("Organization Types")

#     def __str__(self):
#         return self.type


# class ShopUpdateRequest(models.Model):#Rename it to something better

#     user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='update_request')
#     org = models.ForeignKey(ShopOrganizationType, verbose_name=_("Update Request"), on_delete=models.CASCADE, related_name='uodate_to')

#     desc = models.TextField(_("Description"))
#     organization_name = models.CharField(_("Organization Name"), max_length=200, blank=True, null=True)
#     phone = PhoneNumberField(_("Phone Number"), blank=True, null=True)

#     is_verified = models.BooleanField(_("Is Verified"), default=False)

#     def __str__(self):
#         return self.user.email

#     class Meta:
#         managed = True
#         verbose_name = _("User Upgrade Resquest")


# class UserUpdateFiles(models.Model):

#     file_of = models.ForeignKey(ShopUpdateRequest, on_delete=models.CASCADE, related_name='request_file')

#     image = models.ImageField(_("Image"), upload_to="ProfileImages/", default="ProfileImages/download.jpeg", validators=[FileTypeValidator(allowed_types=[ 'image/*'])])

#     def __str__(self):
#         return self.file_of
