from django.test import TestCase
from rest_framework.test import APIRequestFactory
from currencies_exchange.views import CurrencyAPIView


class CurrencyAPIViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CurrencyAPIView.as_view()

    def test_get_currencies(self):
        request = self.factory.get('/currencies/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
