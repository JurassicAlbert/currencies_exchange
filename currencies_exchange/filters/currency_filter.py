import django_filters.rest_framework

from currencies_exchange.models import Currency


class CurrencyFilter(django_filters.FilterSet):
    """
    Filter set for the Currency model.

    This filter set allows filtering currencies based on their name, symbol, and code
    using case-insensitive partial matching.

    Attributes:
        currency_name (django_filters.CharFilter): Filter for currency names.
        currency_symbol (django_filters.CharFilter): Filter for currency symbols.
        currency_code (django_filters.CharFilter): Filter for currency codes.

    Meta:
        model (Currency): The model associated with the filter set.
        fields (list): The list of fields available for filtering.

    Example:
        To filter currencies based on their name:
        filter = CurrencyFilter(data={'currency_name': 'dollar'})
        filtered_currencies = filter.qs
    """

    currency_name = django_filters.CharFilter(lookup_expr='icontains')
    currency_symbol = django_filters.CharFilter(lookup_expr='icontains')
    currency_code = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        """
        Metadata class for the CurrencyFilter.

        Attributes:
            model (Currency): The model associated with the filter set.
            fields (list): The list of fields available for filtering.
        """
        model = Currency
        fields = ['currency_name', 'currency_symbol', 'currency_code']
