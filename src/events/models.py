from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from src.categories.models import Category
from src.locations.models import Address
from src.accounts.models import User
from django.core.validators import MinValueValidator
import os

# Create your models here.

class Guests(models.Model):
    title = models.CharField(max_length=50, verbose_name="Загаловок")
    numeration = models.IntegerField(
        validators=[MinValueValidator(0)], verbose_name='Нумерация')

    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости"

    def __str__(self):
        return self.title


class Events(models.Model):
    categories = models.ForeignKey(Category, related_name="products_categories", on_delete=models.CASCADE, verbose_name="Категория", null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='advertisements', verbose_name="Админ")
    title = models.CharField(max_length=50, verbose_name="Загаловок")
    image = models.ImageField(upload_to="evnts/", null=True,  verbose_name="Фото")
    dateAt = models.DateTimeField( null=True,
        verbose_name="Дата Создания")
    dateEnd = models.DateTimeField( null=True,
        verbose_name="Дата Окончания")
    location = models.ForeignKey(Address, on_delete=models.SET_NULL, related_query_name='events', related_name="events_locations", null=True,
                                blank=True, verbose_name="Локация")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата Создания")
    updatedAt = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменение")
    guests = models.ForeignKey( Guests, related_name="products_guests", on_delete=models.CASCADE, verbose_name="Гости", null=True)
    is_active = models.BooleanField(default=False, verbose_name="Активный")
    is_published = models.BooleanField(
        default=False, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятии"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            if not self.pk:
                if self.image:
                    # image compress with watermark
                    self.compress('image', delete_source=True)
            else:
                if self.image:
                    # image compress without watermark
                    self.compress_without_watermark(
                        'image', delete_source=True)

            this = Events.objects.get(id=self.id)

            if not this.image == self.image:
                if os.path.isfile(this.image.path):
                    os.remove(this.image.path)
        except:
            pass

        super(Events, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Events)
def slider_image(sender, instance, **kwargs):
        # Pass false so FileField doesn't save the model.
        if instance.image:
            instance.image.delete(False)