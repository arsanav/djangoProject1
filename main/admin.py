from django.contrib import admin
from .models import AirPollution, AirPDK, RelevantAirPollution, AirComponentsInfluence, AirDistricts, SpringConditions
from .models import GroundPollutions, Districts
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


class AirComponentsInfluenceResource(resources.ModelResource):
    class Meta:
        model = AirComponentsInfluence


class AirComponentsInfluenceAdmin(ImportExportActionModelAdmin):
    resource_class = AirComponentsInfluenceResource


class AirDistrictsResource(resources.ModelResource):
    class Meta:
        model = AirDistricts


class AirDistrictsAdmin(ImportExportActionModelAdmin):
    resource_class = AirDistrictsResource


class SpringConditionsResource(resources.ModelResource):
    class Meta:
        model = SpringConditions


class SpringConditionsAdmin(ImportExportActionModelAdmin):
    resource_class = SpringConditionsResource


class GroundPollutionsResource(resources.ModelResource):
    class Meta:
        model = GroundPollutions


class GroundPollutionsAdmin(ImportExportActionModelAdmin):
    resource_class = GroundPollutionsResource


class DistrictsResource(resources.ModelResource):
    class Meta:
        model = Districts


class DistrictsAdmin(ImportExportActionModelAdmin):
    resource_class = DistrictsResource


admin.site.register(AirPollution, AirPollutionAdmin)
admin.site.register(AirPDK, AirPDKAdmin)
admin.site.register(RelevantAirPollution, RelevantAirPollutionAdmin)
admin.site.register(AirComponentsInfluence, AirComponentsInfluenceAdmin)
admin.site.register(AirDistricts, AirDistrictsAdmin)
admin.site.register(SpringConditions, SpringConditionsAdmin)
admin.site.register(GroundPollutions, GroundPollutionsAdmin)
admin.site.register(Districts, DistrictsAdmin)


