from django.db import models


# Create your models here.

class AirPDK(models.Model):
    ParameterName = models.TextField('Параметр')
    global_id = models.IntegerField('Глобальный идентификатор')
    UnitOfMeasure = models.CharField('Единицы измерения', max_length=20)
    PDKmr_ASIL = models.FloatField('Абсолютная ПДК')
    PDKss = models.FloatField('ПДКсс')
    DangerClass = models.IntegerField('Класс опасности')

    def __str__(self):
        return self.ParameterName

    class Meta:
        verbose_name = 'ПДК'
        verbose_name_plural = 'ПДК'


class AirDistricts(models.Model):
    District = models.CharField('Район', max_length=100)
    Address = models.CharField('Адрес', max_length=500)
    AirCharacteristic = models.CharField('Уровень влияния', max_length=50)

    def __str__(self):
        return self.Address

    class Meta:
        verbose_name = 'Характеристика районов'
        verbose_name_plural = 'Характеристика районов'

    def as_json(self):
        return dict(
            id=self.id,
            District=self.District,
            Address=self.Address,
            AirCharacteristic=self.AirCharacteristic)


class AirComponentsInfluence(models.Model):
    Component = models.CharField('Компонент', max_length=100)
    DangerType = models.CharField('Класс опасности', max_length=1)
    InfluenceLevel = models.CharField('Уровень влияния', max_length=50)
    Outcome = models.TextField('Последствия')

    def __str__(self):
        return self.Component

    class Meta:
        verbose_name = 'Влияние компонент'
        verbose_name_plural = 'Влияние компонент'


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
    # PDK = models.ForeignKey(AirPDK, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Загрязнение воздуха'
        verbose_name_plural = 'Загрязнение воздуха'


class RelevantAirPollution(models.Model):
    PeriodRel = models.CharField('Период', max_length=10)
    global_idRel = models.IntegerField('Глобальный идентификатор')
    StationNameRel = models.CharField('Станция', max_length=50)
    SurveillanceZoneCharacteristicsRel = models.TextField('Характеристика')
    AdmAreaRel = models.CharField('Округ', max_length=100)
    DistrictRel = models.CharField('Район', max_length=100)
    LocationRel = models.CharField('Адрес', max_length=200)
    ParameterRel = models.TextField('Параметр')
    MonthlyAverageRel = models.FloatField('Абсолютное значение')
    MonthlyAveragePDKssRel = models.CharField('ПДКсс', max_length=50)
    # PDKRel = models.ForeignKey(AirPDK, on_delete=models.CASCADE)
    # DistrictKeyRel = models.ForeignKey(AirDistricts, on_delete=models.CASCADE)
    # ComponentKeyRel = models.ForeignKey(AirComponentsInfluence, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Загрязнение воздуха текущее'
        verbose_name_plural = 'Загрязнение воздуха текущее'

    def as_json(self):
        return dict(
            id=self.id,
            PeriodRel=self.PeriodRel,
            global_idRel=self.global_idRel,
            StationNameRel=self.StationNameRel,
            SurveillanceZoneCharacteristicsRel=self.SurveillanceZoneCharacteristicsRel,
            AdmAreaRel=self.AdmAreaRel,
            DistrictRel=self. DistrictRel,
            LocationRel=self.LocationRel,
            ParameterRel=self.ParameterRel,
            MonthlyAverageRel=self.MonthlyAverageRel,
            MonthlyAveragePDKssRel=self.MonthlyAveragePDKssRel)
