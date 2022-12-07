from django.db import models


class Plan(models.Model):
    name = models.CharField(default="",max_length=255)
    price = models.IntegerField(default=0)
    validity = models.IntegerField(default=0)
    gb_per_day = models.FloatField(default=0.0)
    other_benefits = models.CharField(default="",max_length=255)

    def __str__(self):
        return self.name