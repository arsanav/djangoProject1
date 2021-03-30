from django.contrib import admin
from .models import AirPollution
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields


class AirPollutionResource(resources.ModelResource):
    class Meta:
        model = AirPollution


class AirPollutionAdmin(ImportExportActionModelAdmin):
    resource_class = AirPollutionResource

admin.site.register(AirPollution, AirPollutionAdmin)
