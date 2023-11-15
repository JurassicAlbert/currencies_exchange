from rest_framework import filters, generics
from currencies_exchange.models import Currency
from currencies_exchange.filters import CurrencyFilter
from django_filters.rest_framework import DjangoFilterBackend
from currencies_exchange.serializers import CurrencySerializer


class CurrencyAPIView(generics.ListAPIView):
    """
    API view for retrieving a list of all currencies.

    This view supports filtering, searching, and ordering of currencies.

    Attributes:
        serializer_class (class): The serializer class used to serialize currency objects.
        filter_backends (list): The list of filter backends applied to the view.
        filterset_class (class): The filter class used for filtering the queryset.
        search_fields (list): The list of fields that can be searched.
        ordering_fields (str or tuple): The fields on which ordering is allowed.
        ordering (list): The default ordering applied to the queryset.

    Methods:
        get_queryset(): Retrieves the queryset of all currencies.

    Example:
        To retrieve all currencies:
        GET /api/currencies/
    """

    serializer_class = CurrencySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = CurrencyFilter
    search_fields = ['currency_name', 'currency_symbol', 'currency_code']
    ordering_fields = '__all__'
    ordering = ['currency_code']

    def get_queryset(self):
        """
        Retrieves the queryset of all currencies.

        Returns:
            queryset: The queryset containing all currency objects.
        """
        queryset = Currency.objects.all()
        return queryset
