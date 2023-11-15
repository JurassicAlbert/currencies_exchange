from django import forms
from ..models import CurrencyRate
from datetime import date, timedelta
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator


class CurrencyRateForm(forms.ModelForm):
    """
    Form for handling CurrencyRate model data.

    This form is designed for creating and updating CurrencyRate instances through a web form.

    Meta:
        model (CurrencyRate): The model associated with the form.
        fields (list): The list of fields to be included in the form.

    Methods:
        __init__(*args, **kwargs): Initializes the form and customizes the behavior of some fields.

    Example:
        To handle currency rate data in a web form:
        form = CurrencyRateForm(data=request.POST)
        if form.is_valid():
            currency_rate_instance = form.save()
    """

    class Meta:
        """
        Metadata class for the CurrencyRateForm.

        Attributes:
            model (CurrencyRate): The model associated with the form.
            fields (list): The list of fields to be included in the form.
        """
        model = CurrencyRate
        fields = ['currency_base', 'currency_target', 'history_date']

    def __init__(self, *args, **kwargs):
        """
        Initializes the form and customizes the behavior of some fields.

        The currency_base and currency_target fields are customized to display only the currency codes
        instead of the complete Currency objects. Additionally, the history_date field is validated
        to ensure it falls within a specified range.

        """
        super(CurrencyRateForm, self).__init__()

        # Customize the currency_base and currency_target fields to display only currency codes
        self.fields['currency_base'].queryset = self.fields['currency_base'].queryset.only('currency_code')
        self.fields['currency_base'].widget = forms.Select(
            choices=[(currency.pk, currency.currency_code) for currency in self.fields['currency_base'].queryset])

        self.fields['currency_target'].queryset = self.fields['currency_target'].queryset.only('currency_code')
        self.fields['currency_target'].widget = forms.Select(
            choices=[(currency.pk, currency.currency_code) for currency in self.fields['currency_target'].queryset])

        # Add validators to the history_date field to ensure it falls within a specified range
        self.fields['history_date'].validators.append(MinValueValidator(date(2010, 6, 1)))
        self.fields['history_date'].validators.append(MaxValueValidator(now().date() - timedelta(days=1)))
