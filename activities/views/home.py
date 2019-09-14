from django.http import HttpResponse
from django.shortcuts import render

from activities.models import OutdoorDetail


def index(request):
    outdoor_details = OutdoorDetail.objects.all()
    context = {
        'outdoor_details': outdoor_details,
    }
    return render(request, 'activities/index.html', context)
