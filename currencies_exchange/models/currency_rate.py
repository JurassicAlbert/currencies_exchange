from django.db import models
from .currency import Currency


class CurrencyRate(models.Model):
    id = models.AutoField(editable=False, primary_key=True)
    currency_base = models.ForeignKey(Currency, related_name='base_currency', on_delete=models.CASCADE)
    currency_target = models.ForeignKey(Currency, related_name='target_currency', on_delete=models.CASCADE)
    rate = models.FloatField(verbose_name="Currency Rate", default=1)
    history_date = models.DateTimeField(verbose_name="History date")

    class Meta:
        ordering = ['id', 'currency_base', 'currency_target', 'rate', 'history_date']
        verbose_name_plural = "Currency Rates Historical"
