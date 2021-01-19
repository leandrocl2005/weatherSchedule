from django.db import models


# Create your models here.
class Weather(models.Model):
    class Meta:
        verbose_name_plural = "weathers"
        verbose_name = "weather"

    temperature = models.CharField(max_length=30, verbose_name="Temperatura")
    date = models.CharField(max_length=30, verbose_name="Data")
    time = models.CharField(max_length=30, verbose_name="Hora")
    description = models.CharField(max_length=30, verbose_name="Descrição")
