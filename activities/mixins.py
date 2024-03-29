from django.db import models


class TimeStampMixin(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True