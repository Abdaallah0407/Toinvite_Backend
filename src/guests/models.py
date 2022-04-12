from django.db import models
from django.core.validators import MinValueValidator
from src.accounts.models import User
from src.events.models import Events
# Create your models here.


class GuestsList(models.Model):
    # numeration = models.IntegerField(
    #     validators=[MinValueValidator(0)], verbose_name='Нумерация')
    admin = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='guests_admin', verbose_name="Админ")
    event = models.ForeignKey(Events, on_delete=models.CASCADE,
                              related_name='guests_events', verbose_name="Мероприятие")
    full_name = models.CharField(max_length=50, verbose_name="Полное имя")
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Сотовый телефон')

    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости"

    def __str__(self):
        return self.full_name


class ExcelFileUploud(models.Model):
    excel_file_uploud = models.FileField(upload_to="excel")
