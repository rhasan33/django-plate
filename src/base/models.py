from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', _('active')
        INACTIVE = 'inactive', _('inactive')
        ARCHIVED = 'archived', _('archived')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.JSONField(default=dict)
    updated_by = models.JSONField(default=dict)

    class Meta:
        abstract = True
        app_label = 'base'
