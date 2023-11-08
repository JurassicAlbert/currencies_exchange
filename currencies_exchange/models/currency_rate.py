import logging
import requests
from django.db import models
from .currency import Currency
from datetime import date, timedelta
from django.utils.timezone import now
from ..settings import CURRENCY_API_KEY
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
logger = logging.getLogger(__name__)


class CurrencyRate(models.Model):
    id = models.AutoField(editable=False, primary_key=True)
    currency_base = models.ForeignKey(Currency, related_name='base_currency', on_delete=models.CASCADE)
    currency_target = models.ForeignKey(Currency, related_name='target_currency', on_delete=models.CASCADE)
    rate = models.FloatField(verbose_name='Currency Rate')
    history_date = models.DateField(verbose_name='History date', validators=[
        MinValueValidator(date(2010, 6, 1)),
        MaxValueValidator(now().date() - timedelta(days=1))
    ])

    def __str__(self):
        return f"{self.currency_base.currency_name} to {self.currency_target.currency_name} - Rate: {self.rate}"

    def save(self, *args, **kwargs):
        if not self.rate:
            base_currency_code = self.currency_base.currency_code
            target_currency_code = self.currency_target.currency_code
            history_date = self.history_date.strftime('%Y-%m-%d')
            api_url = f'https://api.currencyapi.com/v3/historical?apikey={CURRENCY_API_KEY}&currencies={target_currency_code}&base_currency={base_currency_code}&date={history_date}'

            try:
                response = requests.get(api_url)
                response.raise_for_status()
                data = response.json()
                rate_value = data['data'][target_currency_code]['value']

                # Update the rate field with the fetched value
                self.rate = rate_value
            except Exception as e:
                if response.status_code == 422:
                    logger.error(f'Failed to fetch currency exchange rate: Unprocessable Entity')
                    raise ValidationError('Failed to fetch currency exchange rate: Unprocessable Entity')
                else:
                    logger.error(f'Failed to fetch currency exchange rate: {e}')
                    raise ValidationError(f'Failed to fetch currency exchange rate: {e}')

        super(CurrencyRate, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id', 'currency_base', 'currency_target', 'rate', 'history_date']
        verbose_name_plural = "Historical Rates"
