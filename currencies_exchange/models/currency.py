from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Currency(models.Model):
    """
    Model representing a currency.

    This model stores information about a currency, including its name, symbol,
    and code.

    Attributes:
        id (models.AutoField): The primary key for the Currency model.
        currency_name (models.TextField): The name of the currency.
        currency_symbol (models.TextField): The symbol of the currency.
        currency_code (models.TextField): The code of the currency.

    Meta:
        ordering (list): The default ordering for the model.
        verbose_name_plural (str): The plural name for the model in the admin interface.

    Example:
        To retrieve currency information:
        currency = Currency.objects.get(id=1)
    """

    id = models.AutoField(editable=False, primary_key=True)
    currency_name = models.TextField(verbose_name="Currency Name", default='US Dollar',
                                     validators=[MinLengthValidator(1), MaxLengthValidator(128)])
    currency_symbol = models.TextField(verbose_name="Currency Symbol", default='$',
                                       validators=[MinLengthValidator(1), MaxLengthValidator(128)])
    currency_code = models.TextField(verbose_name="Currency Code", default='USD',
                                     validators=[MinLengthValidator(1), MaxLengthValidator(128)])

    class Meta:
        """
        Metadata class for the Currency model.

        Attributes:
            ordering (list): The default ordering for the model.
            verbose_name_plural (str): The plural name for the model in the admin interface.
        """
        ordering = ['id', 'currency_name', 'currency_symbol', 'currency_code']
        verbose_name_plural = "Currency"
