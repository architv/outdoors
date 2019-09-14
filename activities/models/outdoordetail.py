import uuid

from django.db import models
from activities.mixins import TimeStampMixin


class OutdoorDetail(TimeStampMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activity_name = models.CharField(max_length=200, null=True)
    sport = models.ForeignKey('activities.Sport', on_delete=models.CASCADE)
    place = models.ForeignKey('activities.Place', on_delete=models.CASCADE)
    guide = models.ForeignKey('activities.Guide', on_delete=models.CASCADE)

    def __str__(self):
        return '{activity_name}, {place}, {guide}'.format(
            activity_name=self.activity_name,
            place=self.place.region,
            guide=self.guide.name)