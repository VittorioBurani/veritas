from django.db import models
from django.core.validators import MinValueValidator


WINE_COLORS = (
    ('red', 'Red'),
    ('rose', 'Rose'),
    ('white', 'White'),
)


class GrapeVariety(models.Model):
    '''Grape Varietiy model'''
    name = models.CharField(max_length=32, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Grape Variety'
        verbose_name_plural = 'Grape Varieties'


class Producer(models.Model):
    '''Wine Producer model'''
    name = models.CharField(max_length=64, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'


class Country(models.Model):
    '''Production Country model'''
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=24, blank=False)

    def __str__(self):
        return f'{self.name} ({self.code})'

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Region(models.Model):
    '''Production Region model'''
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='regions')
    name = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class Wine(models.Model):
    '''Wine model'''
    grape_varieties = models.ManyToManyField(GrapeVariety, related_name='wines')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='wines')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='wines')
    doc = models.CharField(max_length=32, blank=False)
    name = models.CharField(max_length=32, blank=False)
    color = models.CharField(choices=WINE_COLORS, max_length=5, blank=False)
    passito = models.BooleanField(default=False, blank=False)
    sparkling = models.BooleanField(default=False, blank=False)
    year = models.PositiveSmallIntegerField(blank=False)
    quantity = models.PositiveSmallIntegerField(blank=False, default=1, validators=[MinValueValidator(1, 'Quantity must be at least 1.')])

    def __str__(self):
        return f'{self.producer.name} - {self.doc} - {self.name}'

    class Meta:
        verbose_name = 'Wine'
        verbose_name_plural = 'Wines'
