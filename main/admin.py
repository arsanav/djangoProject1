from django.contrib import admin
from .models import AirPollution, AirPDK, RelevantAirPollution
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields


class AirPollutionResource(resources.ModelResource):
    class Meta:
        model = AirPollution


class AirPollutionAdmin(ImportExportActionModelAdmin):
    resource_class = AirPollutionResource


class AirPDKResource(resources.ModelResource):
    class Meta:
        model = AirPDK


class AirPDKAdmin(ImportExportActionModelAdmin):
    resource_class = AirPDKResource


class RelevantAirPollutionResource(resources.ModelResource):
    class Meta:
        model = RelevantAirPollution


class RelevantAirPollutionAdmin(ImportExportActionModelAdmin):
    resource_class = RelevantAirPollutionResource


admin.site.register(AirPollution, AirPollutionAdmin)
admin.site.register(AirPDK, AirPDKAdmin)
admin.site.register(RelevantAirPollution, RelevantAirPollutionAdmin)
