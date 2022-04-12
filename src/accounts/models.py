from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.http import request
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_delete
from src.events.mixins import ImageCompressorMixin
from src.accounts.utils import CLIENT_USER, USER_TYPE


class User(ImageCompressorMixin, AbstractUser):
    email = models.EmailField(
        max_length=255, blank=True, null=True , verbose_name='Почта')
    phone_number = models.CharField(
        max_length=20, blank=True, verbose_name='Сотовый телефон')
    address = models.CharField(max_length=250, blank=True , verbose_name='Адресс')
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    country = models.CharField(max_length=100, blank=True, verbose_name='Страна')
    image = models.ImageField(upload_to='user_images/',
                              null=True, blank=True, verbose_name='Изображение')
    role = models.PositiveSmallIntegerField(
        default=CLIENT_USER, choices=USER_TYPE, verbose_name="Роль")
    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'address', 'city', 'email']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def save(self, *args, **kwargs):
        try:
            if not self.pk:
                if self.image:
                    # image compress with watermark
                    self.compress_without_watermark(
                        'image', delete_source=True, max_width=300, max_height=300)
            else:
                if self.image:
                    # image compress without watermark
                    self.compress_without_watermark(
                        'image', delete_source=True, max_width=300, max_height=300)

            this = User.objects.get(id=self.id)

            # if not this.image == self.image:
            #     if os.path.isfile(this.image.path):
            #         os.remove(this.image.path)

        except:
            pass

        super(User, self).save(*args, **kwargs)


@receiver(pre_delete, sender=User)
def user_image(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=100, unique=True)
    random_code = models.IntegerField()

    class Meta:
        verbose_name = _("Телефон номер")
        verbose_name_plural = _("Телефон номера")

    def __str__(self) -> str:
        return self.phone_number
