from django.contrib import admin
from .models import GrapeVariety, Producer, Country, Region, Wine


class GrapeVarietyModelAdmin(admin.ModelAdmin):
    '''Admin model for Grape Variety'''
    model = GrapeVariety
    search_fields   = [field.name for field in GrapeVariety._meta.get_fields()]
    list_filter     = [field.name for field in GrapeVariety._meta.get_fields()]

admin.site.register(GrapeVariety, GrapeVarietyModelAdmin)


class ProducerModelAdmin(admin.ModelAdmin):
    '''Admin model for Wine Producer'''
    model = Producer
    search_fields   = [field.name for field in Producer._meta.get_fields()]
    list_filter     = [field.name for field in Producer._meta.get_fields()]

admin.site.register(Producer, ProducerModelAdmin)


class CountryModelAdmin(admin.ModelAdmin):
    '''Admin model for Wine Production Country'''
    model = Country
    search_fields   = [field.name for field in Country._meta.get_fields()]
    list_filter     = [field.name for field in Country._meta.get_fields()]

admin.site.register(Country, CountryModelAdmin)


class RegionModelAdmin(admin.ModelAdmin):
    '''Admin model for Wine Production Country'''
    model = Region
    search_fields   = [field.name for field in Region._meta.get_fields()]
    list_filter     = [field.name for field in Region._meta.get_fields()]

admin.site.register(Region, RegionModelAdmin)


class WineModelAdmin(admin.ModelAdmin):
    '''Admin model for Wine'''
    model = Wine
    search_fields   = [field.name for field in Wine._meta.get_fields()]
    list_filter     = [field.name for field in Wine._meta.get_fields()]

admin.site.register(Wine, WineModelAdmin)
