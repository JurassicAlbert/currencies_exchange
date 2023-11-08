from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Currency(models.Model):
    id = models.AutoField(editable=False, primary_key=True)
    currency_name = models.TextField(verbose_name="Currency Name", default='US Dollar',
                                     validators=[MinLengthValidator(1), MaxLengthValidator(128)])
    currency_symbol = models.TextField(verbose_name="Currency Symbol", default='$',
                                       validators=[MinLengthValidator(1), MaxLengthValidator(128)])
    currency_code = models.TextField(verbose_name="Currency Code", default='USD',
                                     validators=[MinLengthValidator(1), MaxLengthValidator(128)])

    class Meta:
        ordering = ['id', 'currency_name', 'currency_symbol', 'currency_code']
        verbose_name_plural = "Currency"
