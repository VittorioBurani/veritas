# Generated by Django 5.0.4 on 2024-04-29 00:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='GrapeVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': 'Grape Variety',
                'verbose_name_plural': 'Grape Varieties',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'Producer',
                'verbose_name_plural': 'Producers',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='wine_cellar.country')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('color', models.CharField(choices=[('red', 'Red'), ('rose', 'Rose'), ('white', 'White')], max_length=5)),
                ('passito', models.BooleanField(default=False)),
                ('sparkling', models.BooleanField(default=False)),
                ('year', models.PositiveSmallIntegerField()),
                ('quantity', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Quantity must be at least 1.')])),
                ('grape_varieties', models.ManyToManyField(related_name='wines', to='wine_cellar.grapevariety')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wines', to='wine_cellar.producer')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wines', to='wine_cellar.region')),
            ],
            options={
                'verbose_name': 'Wine',
                'verbose_name_plural': 'Wines',
            },
        ),
    ]
