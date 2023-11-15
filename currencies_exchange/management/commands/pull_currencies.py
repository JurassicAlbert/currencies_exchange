import requests
from currencies_exchange.models import Currency
from django.core.management.base import BaseCommand
from currencies_exchange.settings import CURRENCY_API_KEY


class Command(BaseCommand):
    """
    Django management command for getting data from an external API and saving it to the database.

    This command retrieves information about currencies from an external API and updates
    the Currency model in the database with the fetched data.

    Attributes:
        help (str): A short description of the command's purpose.

    Methods:
        handle(*args, **options): Executes the command's logic.

    Example:
        To pull currencies data from the external API and update database:
        python manage.py pull_currencies
    """

    help = 'Get data from external API and save it to the database'

    def handle(self):
        """
        Executes the command's logic.

        Fetches data from an external API and updates the Currency model in the database
        with the fetched information.

        Args:
            *args: Additional positional arguments.
            **options: Additional keyword arguments.
        """
        url = f'https://api.currencyapi.com/v3/currencies?apikey={CURRENCY_API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            all_currencies = response.json().get('data', {})
            for currency_code, currency_data in all_currencies.items():
                currency_name = currency_data.get('name')
                if currency_name:
                    currency, created = Currency.objects.get_or_create(
                        currency_code=currency_code,
                        defaults={
                            'currency_name': currency_name,
                            'currency_symbol': currency_data.get('symbol'),
                            'currency_code': currency_code,
                        }
                    )
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f'Successfully created Currency: {currency.currency_name}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Currency already exists: {currency.currency_name}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Invalid currency name for code {currency_code}'))
        else:
            self.stdout.write(
                self.style.ERROR(f'Failed to fetch data from the API. Status code: {response.status_code}'))
