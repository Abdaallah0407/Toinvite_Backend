# Generated by Django 3.2.12 on 2022-04-14 07:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Город/Область')),
                ('numeration', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Нумерация')),
            ],
            options={
                'verbose_name': 'Город/Область',
                'verbose_name_plural': 'Города/Области',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('latitude', models.FloatField(default=0, verbose_name='Широта')),
                ('longitude', models.FloatField(default=0, verbose_name='Долгота')),
                ('numeration', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Нумерация')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='districts', to='locations.city', verbose_name='Город/Область')),
            ],
            options={
                'verbose_name': 'Адрес/Район',
                'verbose_name_plural': 'Адрес/Район',
            },
        ),
    ]
