# Generated by Django 3.2.12 on 2022-04-04 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Главная Категория', 'verbose_name_plural': 'Категории Ивентов'},
        ),
    ]
