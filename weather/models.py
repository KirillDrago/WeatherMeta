from django.db import models


class Weather(models.Model):
    date = models.DateField()
    temperature = models.IntegerField(null=True)
    weather_description = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.date} - {self.temperature} - {self.weather_description}"
