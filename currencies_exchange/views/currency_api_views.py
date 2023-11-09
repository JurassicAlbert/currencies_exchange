import django_filters
from rest_framework import generics
from currencies_exchange.models import Currency
from currencies_exchange.filters import CurrencyFilter
from currencies_exchange.serializers import CurrencySerializer


# class CurrencyAPIView(APIView):
#     """Currency API for fetch a list of all currencies"""
#
#     def get(self, request):
#         all_currencies = Currency.objects.all()
#         serialized_currencies = CurrencySerializer(all_currencies, many=True)
#         if not serialized_currencies:
#             return Response("Unable to find currencies data", status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response(serialized_currencies.data, status=status.HTTP_200_OK)


class CurrencyAPIView(generics.ListAPIView):
    """Currency API for fetch a list of all currencies"""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = CurrencyFilter
