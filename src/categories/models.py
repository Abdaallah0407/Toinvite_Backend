from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Загаловок")
    icon = models.FileField(upload_to="categories/",
                              blank=True, null=True,  verbose_name="Фото")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата Создания")
    updatedAt = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменение")

    class Meta:
        verbose_name = "Главная Категория"
        verbose_name_plural = "Категории Ивентов"

    def __str__(self):
        return self.title