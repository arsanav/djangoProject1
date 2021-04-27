from django.shortcuts import render
from .models import RelevantAirPollution, AirDistricts, AirPDK, AirComponentsInfluence, SpringConditions
from django.core import serializers


def master(request):
    rel_air_pollutions = serializers.serialize('json', RelevantAirPollution.objects.all())
    air_districts = serializers.serialize('json', AirDistricts.objects.all())
    air_pdk = serializers.serialize('json', AirPDK.objects.all())
    air_components_influence = serializers.serialize('json', AirComponentsInfluence.objects.all())
    spring_conditions = serializers.serialize('json', SpringConditions.objects.all())
    return render(request, 'main/master.html',
                  {'air_districts': air_districts,
                   'rel_air_pollutions': rel_air_pollutions,
                   'air_pdk': air_pdk,
                   'air_components_influence': air_components_influence,
                   'spring_conditions': spring_conditions})


def maps(request):
    return render(request, 'main/maps.html')
