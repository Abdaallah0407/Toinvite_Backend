from django.db import models

# Create your models here.
class BackCall(models.Model):

    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Электронный адресс", null=True)
    description = models.TextField("Вопрос или пожeлание", null=True)
    data_added = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Обратный звонок и вопрос"
        verbose_name_plural = "Обратные звонки и вопросы"