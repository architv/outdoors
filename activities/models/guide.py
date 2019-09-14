import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from activities.mixins import TimeStampMixin

class Guide(TimeStampMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    place = models.ForeignKey('activities.Place', on_delete=models.CASCADE)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)