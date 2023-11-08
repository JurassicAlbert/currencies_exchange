import django
from django.urls import reverse
from django.test import TestCase
from rest_framework.views import status
from currencies_exchange.models import Currency
from rest_framework.test import APIRequestFactory
from currencies_exchange.views import CurrencyAPIView
from currencies_exchange.serializers import CurrencySerializer


class CurrencyAPIViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CurrencyAPIView.as_view()
        django.setup()
        self.url = reverse('currency-api')

    def test_get_currencies_from_api(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_currencies_from_db(self):
        all_currencies = Currency.objects.all()
        serialized_currencies = CurrencySerializer(all_currencies, many=True)
        self.assertTrue(serialized_currencies, serialized_currencies)
