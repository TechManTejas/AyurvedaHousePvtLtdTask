from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from plansapi import views as plansapi_views
from rechargeapi import views as rechargeapi_views

router = DefaultRouter()
router.register('plans', plansapi_views.PlanModelViewset, basename='plans')
router.register('recharge', rechargeapi_views.RechargeModelViewset, basename='recharge')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
