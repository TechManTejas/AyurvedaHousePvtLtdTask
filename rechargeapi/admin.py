from django.contrib import admin
from .models import Recharge


@admin.register(Recharge)
class RechargeAdmin(admin.ModelAdmin):
    list_display = ["id", "recharged_pack_id"]
