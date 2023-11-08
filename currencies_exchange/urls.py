from django.urls import path
from django.contrib import admin
from rest_framework import routers

from currencies_exchange.views import currency_api_views

router = routers.DefaultRouter()
router.register(r'currency', currency_api_views.CurrencyAPIView, basename="Currency")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currency/', currency_api_views.CurrencyAPIView.as_view(), name='currency-api')
]
