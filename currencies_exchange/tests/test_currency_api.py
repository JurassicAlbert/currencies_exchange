import django
from django.urls import reverse
from django.test import TestCase
from rest_framework.views import status
from currencies_exchange.models import Currency
from rest_framework.test import APIRequestFactory
from currencies_exchange.views import CurrencyAPIView
from currencies_exchange.serializers import CurrencySerializer


class CurrencyAPIViewTest(TestCase):
    """
    Test case for the CurrencyAPIView.

    This test case includes methods to test the behavior of the CurrencyAPIView.

    Attributes:
        factory (APIRequestFactory): The APIRequestFactory instance for creating requests.
        view (callable): The view function for the CurrencyAPIView.
        url (str): The URL for the CurrencyAPIView.

    Methods:
        setUp(): Set up the necessary resources for the test case.
        test_get_currencies_from_api(): Test the retrieval of currencies from the API.
        test_get_currencies_from_db(): Test the retrieval of currencies from the database.

    Example:
        To run the tests:
        python manage.py test currencies_exchange.tests.CurrencyAPIViewTest
    """

    def setUp(self):
        """
        Set up the necessary resources for the test case.
        """
        self.factory = APIRequestFactory()
        self.view = CurrencyAPIView.as_view()
        django.setup()
        self.url = reverse('currency-api')

    def test_get_currencies_from_api(self):
        """
        Test the retrieval of currencies from the API.

        This test sends a GET request to the CurrencyAPIView and asserts that
        the response status code is HTTP_200_OK.

        Example:
            To test the API endpoint:
            python manage.py test currencies_exchange.tests.CurrencyAPIViewTest.test_get_currencies_from_api
        """
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_currencies_from_db(self):
        """
        Test the retrieval of currencies from the database.

        This test retrieves all currencies from the database, serializes them,
        and asserts that the serialized data is not empty.

        Example:
            To test the database retrieval:
            python manage.py test currencies_exchange.tests.CurrencyAPIViewTest.test_get_currencies_from_db
        """
        all_currencies = Currency.objects.all()
        serialized_currencies = CurrencySerializer(all_currencies, many=True)
        self.assertTrue(serialized_currencies, serialized_currencies)
