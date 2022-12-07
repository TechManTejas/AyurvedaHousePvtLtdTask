from django.db import models
from plansapi.models import Plan


class Recharge(models.Model):
    recharged_pack_id = models.ForeignKey(to=Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.recharged_pack_id
