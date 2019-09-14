import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from activities.mixins import TimeStampMixin

class Place(TimeStampMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    lat = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=8)
    lng = models.DecimalField(_('Longitude'), max_digits=11, decimal_places=8)