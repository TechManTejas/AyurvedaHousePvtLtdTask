from rest_framework import viewsets
from .models import Plan
from .serializers import PlanSerializer

class PlanModelViewset(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    http_method_names = ["GET"]
