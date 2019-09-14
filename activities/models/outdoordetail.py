import uuid

from django.db import models
from activities.mixins import TimeStampMixin


class OutdoorDetail(TimeStampMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sport = models.ForeignKey('activities.Sport', on_delete=models.CASCADE)
    place = models.ForeignKey('activities.Place', on_delete=models.CASCADE)
    guide = models.ForeignKey('activities.Guide', on_delete=models.CASCADE)