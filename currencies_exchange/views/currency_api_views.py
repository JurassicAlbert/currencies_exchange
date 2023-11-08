from rest_framework.response import Response
from currencies_exchange.models import Currency
from rest_framework.views import APIView, status
from currencies_exchange.serializers import CurrencySerializer


class CurrencyAPIView(APIView):
    """Currency API for fetch a list of all currencies"""

    def get(self, request):
        all_currencies = Currency.objects.all()
        serialized_currencies = CurrencySerializer(all_currencies, many=True)
        if not serialized_currencies:
            return Response("Unable to find currencies data", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serialized_currencies.data, status=status.HTTP_200_OK)
