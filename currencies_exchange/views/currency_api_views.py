from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from currencies_exchange.models import Currency
from currencies_exchange.filters import CurrencyFilter
from currencies_exchange.serializers import CurrencySerializer


class CurrencyAPIView(generics.ListAPIView):
    """Currency API for fetch a list of all currencies"""
    # queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = CurrencyFilter
    search_fields = ['currency_name', 'currency_symbol', 'currency_code']
    ordering_fields = '__all__'
    ordering = ['currency_code']

    def get_queryset(self):
        queryset = Currency.objects.all()
        return queryset
