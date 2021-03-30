from django.shortcuts import render
from .models import AirPollution


def master(request):
    air_pollutions = AirPollution.objects.all()
    return render(request, 'main/master.html', {'data': 'Питер', 'air_pollutions': air_pollutions})
