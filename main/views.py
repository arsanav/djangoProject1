from django.shortcuts import render
from .models import RelevantAirPollution, AirDistricts, AirPDK, AirComponentsInfluence, SpringConditions
from .models import GroundPollutions, Districts
from django.core import serializers
import warnings
import itertools
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def master(request):
    rel_air_pollutions = serializers.serialize('json', RelevantAirPollution.objects.all())
    air_districts = serializers.serialize('json', AirDistricts.objects.all())
    air_pdk = serializers.serialize('json', AirPDK.objects.all())
    air_components_influence = serializers.serialize('json', AirComponentsInfluence.objects.all())
    spring_conditions = serializers.serialize('json', SpringConditions.objects.all())
    ground_pollutions = serializers.serialize('json', GroundPollutions.objects.all())
    return render(request, 'main/master.html',
                  {'air_districts': air_districts,
                   'rel_air_pollutions': rel_air_pollutions,
                   'air_pdk': air_pdk,
                   'air_components_influence': air_components_influence,
                   'spring_conditions': spring_conditions,
                   'ground_pollutions': ground_pollutions})


def maps(request):
    districts = serializers.serialize('json', Districts.objects.all())
    air_districts = serializers.serialize('json', AirDistricts.objects.all())
    spring_conditions = serializers.serialize('json', SpringConditions.objects.all())
    ground_pollutions = serializers.serialize('json', GroundPollutions.objects.all())
    return render(request, 'main/maps.html', {'districts': districts,
                                              'air_districts': air_districts,
                                              'spring_conditions': spring_conditions,
                                              'ground_pollutions': ground_pollutions})


def co(request):
    art = pd.read_csv('http://127.0.0.1:8800/9.csv', delimiter=';', names=['datetime', 'District', 'location', 'namel', 'value'])
    art1 = art[art.District == 'район Новокосино'][['datetime', 'value']]
    art1['date'] = pd.to_datetime(art1[['datetime']].stack(), format='%d.%m.%Y').unstack()
    art1['val'] = pd.to_numeric(art1[['value']].stack()).unstack()
    art2 = art1[['date', 'val']]
    art2 = art2.resample('MS', on='date').mean()
    art2 = art2.fillna(art2.bfill())
    mod = sm.tsa.statespace.SARIMAX(art2,
                                    order=(1, 1, 1),
                                    seasonal_order=(0, 0, 0, 60),
                                    enforce_stationarity=False,
                                    enforce_invertibility=False)
    results = mod.fit()
    pred = results.get_prediction(start=pd.to_datetime('2016-02-01'), dynamic=False)
    pred_ci = pred.conf_int()
    ax = art2.plot(label='Данные',figsize=(15.5, 7))
    pred.predicted_mean.plot(ax=ax, label='Прогноз', alpha=.7)
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.2)
    ax.set_xlabel('Date')
    ax.set_ylabel('CO Levels')
    plt.ylim(0, 1)
    plt.legend()
    plt.savefig('C:\\Users\Арсений\PycharmProjects\djangoProject1\main\static\json\ig.png')
    ax = art2.plot(label='Данные', figsize=(20, 15))
    pred_uc = results.get_forecast(steps=2)
    pred_ci = pred_uc.conf_int()
    pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.25)
    next1 = pred_uc.predicted_mean[0]
    return render(request, 'main/co.html', {'next1': next1, 'current': art2['val'][60]})


def climat(request):
    return render(request, 'main/climat.html')
