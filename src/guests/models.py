from django.db import models
from django.core.validators import MinValueValidator
from src.accounts.models import User
from src.events.models import Events
from toinvite_core import settings
from twilio.rest import Client
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class GuestsAdmin(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username}"
        else:
            return f"{self.id}"

    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости в Админке"


class GuestsList(models.Model):
    # numeration = models.IntegerField(
    #     validators=[MinValueValidator(0)], verbose_name='Нумерация')
    admin = models.ForeignKey(GuestsAdmin, on_delete=models.CASCADE,
                              related_name='guests_admin', verbose_name="Админ", blank=True, null=True,)
    event = models.ForeignKey(
        Events, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=50, verbose_name="Полное имя")
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Сотвый Телефон")
    number_secand = PhoneNumberField(
        unique=True, null=False, blank=True, verbose_name="Домашний телефон")
    status = models.BooleanField(
        default=None, blank=True, null=True, verbose_name="Статус")

    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.pk:  # Only if the instance is being created the code is executed
            phone_numbers = [
                profile.phone_number for profile in GuestsList.objects.all()]

            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)
            print('Isa')
            for phone_number in phone_numbers:

                # phone_number = i.phone_number
                # phone_number = '+' + phone_number

                if phone_number:
                    print('ipsum')
                    message = client.messages.create(
                        body='{}  Вы были приглашены на {} !!! Которая состоится 15 декабря в 11.00 ресторан Ала-Тоо.'.format(
                            self.full_name, self.event),
                        from_='+19592511918',
                        to='{}'.format(
                            self.phone_number))
                    print(message.sid)

        super().save(*args, **kwargs)


class ExcelFileUploud(models.Model):
    excel_file_uploud = models.FileField(upload_to="excel")
