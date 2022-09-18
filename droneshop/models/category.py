from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models.profileModel import UserProfile
import uuid

class Category(models.Model):

    uuid = models.UUIDField(_("PID"), max_length=20, unique=True, editable=False, primary_key=True, default=uuid.uuid4)

    name = models.CharField(_('Name'), max_length=20, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
