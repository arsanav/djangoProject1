from django.db import models


# Create your models here.
class AirPollution(models.Model):
    Period = models.CharField('Период', max_length=10)
    global_id = models.IntegerField('Глобальный идентификатор')
    StationName = models.CharField('Станция', max_length=50)
    SurveillanceZoneCharacteristics = models.TextField('Характеристика')
    AdmArea = models.CharField('Округ', max_length=100)
    District = models.CharField('Район', max_length=100)
    Location = models.CharField('Адрес', max_length=200)
    Parameter = models.TextField('Параметр')
    MonthlyAverage = models.FloatField('Абсолютное значение')
    MonthlyAveragePDKss = models.CharField('ПДКсс', max_length=50)


    class Meta:
        verbose_name = 'Загрязнение воздуха'
        verbose_name_plural = 'Загрязнение воздуха'
