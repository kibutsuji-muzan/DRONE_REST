from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models.profileModel import UserProfile
import uuid

class Portfolio(models.Model):

    uuid = models.UUIDField(_("UUID"), primary_key = True, default=uuid.uuid4, editable=False, unique=True)

    owner = models.OneToOneField(UserProfile, verbose_name=_("Portfolio Of"), on_delete=models.CASCADE, related_name="Portfolio")

    title = models.CharField(_("Title"), max_length=50)
    bio = models.TextField(_("Biography"), max_length=300)

    def __str__(self):
        return self.owner.email

    class Meta:
        managed = True
        verbose_name = _('Protfolio')

class PortfolioImage(models.Model):
    uuid = models.UUIDField(_("UUID"), primary_key = True, default=uuid.uuid4, editable=False, unique=True)

    image_of = models.ForeignKey(Portfolio, verbose_name=_("Image Of"), on_delete=models.CASCADE)

    image = models.ImageField(_("Porfolio Image"), upload_to="Portfolio/")
    alt_txt = models.CharField(_("Alternative Text"), max_length=15)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        verbose_name = _('Portfolio Image')

class PortfolioDetailValue(models.Model):

    uuid = models.UUIDField(_("UUID"), primary_key = True, default=uuid.uuid4, editable=False, unique=True)

    portfolio = models.ForeignKey(Portfolio, verbose_name=_("Portfolio Details"), on_delete=models.CASCADE, related_name="portfolio_details")

    detail_key = models.CharField(_("Detail Key"), max_length=20)
    value_key = models.CharField(_("Value Key"), max_length=50)

    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        verbose_name = _("Portfolio Detail & Values")