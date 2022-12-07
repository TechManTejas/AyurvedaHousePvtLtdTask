from rest_framework import viewsets
from .models import Recharge
from .serializers import RechargeSerializer


class RechargeModelViewset(viewsets.ModelViewSet):
    queryset = Recharge.objects.all()
    serializer_class = RechargeSerializer
