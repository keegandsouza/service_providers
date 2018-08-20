from tastypie import fields
from tastypie.resources import ALL
from tastypie.contrib.gis.resources import ModelResource
from tastypie.authorization import Authorization
from .models import Provider, ServiceArea, Language, Currency


class LanguageResource(ModelResource):
    class Meta:
        queryset = Language.objects.all()
        resource_name = 'language'


class CurrencyResource(ModelResource):
    class Meta:
        queryset = Currency.objects.all()
        resource_name = 'currency'


class ProviderResource(ModelResource):
    currency = fields.ToOneField(CurrencyResource, attribute='currency', null=True, full=True)
    language = fields.ToOneField(LanguageResource, attribute='language', null=True, full=True)

    class Meta:
        queryset = Provider.objects.all()
        resource_name = 'provider'
        authorization = Authorization()


class ServiceAreaResource(ModelResource):
    provider = fields.ToOneField(ProviderResource, attribute='provider', null=True, full=True)

    class Meta:
        queryset = ServiceArea.objects.all()
        resource_name = 'service_area'
        authorization = Authorization()
        filtering = {
            'polygon': ALL,
        }

    def hydrate_polygon(self, bundle):
        """Puts in a None value for a polygon

        Necessary since tastypie's default hydration fails to serialize the polygon field itself
        if the field is not passed while updating (PUT requests) a service_provdier

        Arguments:
            bundle {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        if 'polygon' not in bundle.data.keys():
            bundle.data["polygon"] = None
        return bundle
