from rest_framework import serializers
from wine_cellar.models import GrapeVariety, Producer, Country, Region, Wine


class GrapeVarietySerializer(serializers.ModelSerializer):
    '''GrapeVariety Model Serializer'''
    class Meta:
        model = GrapeVariety
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    '''Producer Model Serializer'''
    class Meta:
        model = Producer
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    '''Country Model Serializer'''
    class Meta:
        model = Country
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    '''Region Model Serializer'''
    class Meta:
        model = Region
        fields = '__all__'


class CountryDisplaySerializer(CountrySerializer):
    '''Country Display Model Serializer'''
    regions = RegionSerializer(many=True)


class RegionDisplaySerializer(RegionSerializer):
    '''Region Display Model Serializer'''
    country = CountrySerializer()


class WineSerializer(serializers.ModelSerializer):
    '''Wine Model Serializer'''
    class Meta:
        model = Wine
        fields = '__all__'


class WineDisplaySerializer(WineSerializer):
    '''Wine Display Model Serializer'''
    grape_varieties = GrapeVarietySerializer(many=True)
    producer = ProducerSerializer()
    region = RegionDisplaySerializer()
