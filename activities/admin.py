from django.contrib import admin

# Register your models here.

from .models import Place, OutdoorDetail, Sport, Guide

admin.site.register(Guide)
admin.site.register(OutdoorDetail)
admin.site.register(Place)
admin.site.register(Sport)