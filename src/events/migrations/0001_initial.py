# Generated by Django 3.2.12 on 2022-04-26 11:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('locations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Загаловок')),
                ('numeration', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Нумерация')),
            ],
            options={
                'verbose_name': 'Гость',
                'verbose_name_plural': 'Гости',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Загаловок')),
                ('image', models.ImageField(null=True, upload_to='evnts/', verbose_name='Фото')),
                ('dateAt', models.DateTimeField(null=True, verbose_name='Дата Создания')),
                ('dateEnd', models.DateTimeField(null=True, verbose_name='Дата Окончания')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Дата изменение')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to=settings.AUTH_USER_MODEL, verbose_name='Админ')),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_categories', to='categories.category', verbose_name='Категория')),
                ('guests', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_guests', to='events.guests', verbose_name='Гости')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_locations', related_query_name='events', to='locations.address', verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятии',
            },
        ),
    ]
