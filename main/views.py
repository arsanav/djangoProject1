from django.shortcuts import render
from .models import RelevantAirPollution, AirDistricts
from django.core import serializers


def master(request):
    rel_air_pollutions = serializers.serialize('json', RelevantAirPollution.objects.all())
    air_districts = serializers.serialize('json', AirDistricts.objects.all())
    return render(request, 'main/master.html', {'air_districts': air_districts, 'rel_air_pollutions': rel_air_pollutions})
