from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models.profileModel import UserProfile
import uuid

class Blog(models.Model):

    id = models.UUIDField(_("UUID"), default=uuid.uuid4, primary_key=True, editable=False)

    user = models.ForeignKey(UserProfile, verbose_name=_("Blog From"), on_delete=models.CASCADE, related_name="blogs")

    title = models.CharField(_("Title"), max_length=100)
    content = models.CharField(_("Content"), max_length=3000)

    def __str__(self):

        return self.user.email

    class Meta:
        managed=True
        verbose_name = _("Blog")

class blog_image(models.Model):

    id = models.UUIDField(_("UUID"), default=uuid.uuid4, primary_key=True, editable=False)

    blog = models.OneToOneField(Blog, verbose_name=_("Blog Image"), on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), default="blogs/")

    def __str__(self):
        return self.blog.title

    class Meta:
        managed=True 
        verbose_name = _("Blog Image")