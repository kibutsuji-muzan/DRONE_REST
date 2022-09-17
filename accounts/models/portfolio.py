from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models.profileModel import UserProfile
import uuid
from upload_validator import FileTypeValidator


validator = FileTypeValidator(
    allowed_types=['application/msword'],
    allowed_extensions=['.doc', '.docx']
)

class Portfolio(models.Model):

    owner = models.OneToOneField(UserProfile, verbose_name=_("Portfolio Of"), on_delete=models.CASCADE, related_name="portfolio", primary_key=True, editable=True)

    title = models.CharField(_("Title"), max_length=50)
    bio = models.TextField(_("Biography"), max_length=300)
    links = models.URLField(_("External Links"), max_length=50, blank=False, null=True)

    def __str__(self):
        return self.owner.email

    class Meta:
        managed = True
        verbose_name = _('Protfolio')


class PortfolioPost(models.Model):

    portfolio = models.ForeignKey(Portfolio, verbose_name=_("Portfolio"), on_delete=models.CASCADE, related_name="posts")

    caption = models.TextField(_("Caption"), max_length=500)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.portfolio.owner.email

class PostImage(models.Model):
    uuid = models.UUIDField(_("UUID"), primary_key = True, default=uuid.uuid4, editable=False, unique=True)

    image_of = models.ForeignKey(PortfolioPost, verbose_name=_("Image Of"), on_delete=models.CASCADE, related_name='post_image')

    image = models.ImageField(_("Porfolio Image"), upload_to="Portfolio/", validators=[FileTypeValidator(allowed_types=[ 'image/*'])])
    alt_txt = models.CharField(_("Alternative Text"), max_length=15, default='portfolio image')

    class Meta:
        managed = True
        verbose_name = _('Portfolio Image')
