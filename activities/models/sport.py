import uuid

from django.db import models
from activities.mixins import TimeStampMixin

class Sport(TimeStampMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    terrain = models.CharField(max_length=200)