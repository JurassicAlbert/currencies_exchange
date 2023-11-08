from django import forms
from ..models import CurrencyRate
from datetime import date, timedelta
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator


class CurrencyRateForm(forms.ModelForm):
    class Meta:
        model = CurrencyRate
        fields = ['currency_base', 'currency_target', 'history_date']

    def __init__(self, *args, **kwargs):
        super(CurrencyRateForm, self).__init__(*args, **kwargs)
        self.fields['currency_base'].queryset = self.fields['currency_base'].queryset.only('currency_code')
        self.fields['currency_base'].widget = forms.Select(
            choices=[(currency.pk, currency.currency_code) for currency in self.fields['currency_base'].queryset])
        self.fields['currency_target'].queryset = self.fields['currency_target'].queryset.only('currency_code')
        self.fields['currency_target'].widget = forms.Select(
            choices=[(currency.pk, currency.currency_code) for currency in self.fields['currency_target'].queryset])
        self.fields['history_date'].validators.append(MinValueValidator(date(2010, 6, 1)))
        self.fields['history_date'].validators.append(MaxValueValidator(now().date() - timedelta(days=1)))
