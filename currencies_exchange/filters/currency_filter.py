import django_filters.rest_framework

from currencies_exchange.models import Currency


class CurrencyFilter(django_filters.FilterSet):
    currency_name = django_filters.CharFilter(lookup_expr='icontains')
    currency_symbol = django_filters.CharFilter(lookup_expr='icontains')
    currency_code = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Currency
        fields = ['currency_name', 'currency_symbol', 'currency_code']
        # ordering = ['currency_name', 'currency_symbol', 'currency_code']
