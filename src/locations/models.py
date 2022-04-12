from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _



####################################################################################
class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Город/Область')
    numeration = models.IntegerField(
        validators=[MinValueValidator(0)], verbose_name='Нумерация')

    class Meta:
        verbose_name = _("Город/Область")
        verbose_name_plural = _("Города/Области")

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey(
        City, null=True, on_delete=models.SET_NULL, blank=True, verbose_name='Город/Область', related_name='districts')
    name = models.CharField(max_length=100, verbose_name='Название')
    latitude = models.FloatField(default=0, verbose_name='Широта')
    longitude = models.FloatField(default=0, verbose_name='Долгота')
    numeration = models.IntegerField(
        validators=[MinValueValidator(0)], verbose_name='Нумерация')

    class Meta:
        verbose_name = _("Адрес/Район")
        verbose_name_plural = _("Адрес/Район")

    def __str__(self):
        return self.name
