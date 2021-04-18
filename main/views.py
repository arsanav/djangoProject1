from django.shortcuts import render
from .models import AirPollution, RelevantAirPollution
from django.core import serializers
import json


def master(request):
    rel_air_pollution = RelevantAirPollution.objects.all()
    rel_air_pollutions = serializers.serialize('json', rel_air_pollution)
    return render(request, 'main/master.html', {'data': 'Питер', 'rel_air_pollutions': rel_air_pollutions})
