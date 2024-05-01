
from django_filters import rest_framework as filters
from custom.utils.filterset_utils import get_model_fields_filters
from wine_cellar.models import GrapeVariety, Producer, Country, Region, Wine


class GrapeVarietyFilter(filters.FilterSet):
    '''Filter class for GrapeVariety Serializers'''
    class Meta:
        model = GrapeVariety
        fields = get_model_fields_filters(GrapeVariety, exclude=['wines'])


class ProducerFilter(filters.FilterSet):
    '''Filter class for Producer Serializers'''
    class Meta:
        model = Producer
        fields = get_model_fields_filters(Producer, exclude=['wines'])


class CountryFilter(filters.FilterSet):
    '''Filter class for Country Serializers'''
    has_region = filters.Filter(field_name='regions', lookup_expr='in')

    class Meta:
        model = Country
        fields = get_model_fields_filters(Country, exclude=['regions'])


class RegionFilter(filters.FilterSet):
    '''Filter class for Region Serializers'''
    class Meta:
        model = Region
        fields = {
            **get_model_fields_filters(Region, exclude=['wines']),
            **get_model_fields_filters(Country, prefix='country__', exclude=['regions']),
        }


class WineFilter(filters.FilterSet):
    '''Filter class for Wine Serializers'''
    has_grape = filters.Filter(field_name='grape_varieties', lookup_expr='in')

    class Meta:
        model = Wine
        fields = {
            **get_model_fields_filters(Wine, exclude=['grape_varieties']),
            **get_model_fields_filters(Producer, prefix='producer__', exclude=['wines']),
            **get_model_fields_filters(Region, prefix='region__', exclude=['wines']),
            **get_model_fields_filters(Country, prefix='region__country__', exclude=['regions']),
        }
