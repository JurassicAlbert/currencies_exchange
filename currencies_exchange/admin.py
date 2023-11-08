from django.db.models import F
from django.contrib import admin
from .forms import CurrencyRateForm
from .models import Currency, CurrencyRate
from django.contrib.auth.models import Group, User

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    search_fields = ['currency_name', 'currency_code']
    list_display = ['id', 'currency_name', 'currency_symbol', 'currency_code']
    list_filter = ['currency_code', 'currency_name', 'currency_symbol']
    list_per_page = 10

    def has_add_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False


class CurrencyBaseCodeFilter(admin.SimpleListFilter):
    title = 'Currency Base Code'
    parameter_name = 'currency_base_code'

    def lookups(self, request, model_admin):
        queryset = CurrencyRate.objects.values_list('currency_base__currency_code', flat=True).distinct()
        return [(code, code) for code in queryset]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(currency_base__currency_code=self.value())
        return queryset


class CurrencyTargetCodeFilter(admin.SimpleListFilter):
    title = 'Currency Target Code'
    parameter_name = 'currency_target_code'

    def lookups(self, request, model_admin):
        queryset = CurrencyRate.objects.values_list('currency_target__currency_code', flat=True).distinct()
        return [(code, code) for code in queryset]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(currency_target__currency_code=self.value())
        return queryset


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    search_fields = ['currency_base__currency_code', 'currency_target__currency_code']
    list_display = ['id', 'currency_base_code', 'currency_target_code', 'rate', 'history_date']
    form = CurrencyRateForm
    list_per_page = 10
    list_filter = [CurrencyBaseCodeFilter, CurrencyTargetCodeFilter]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(currency_base_code=F('currency_base__currency_code'),
                                 currency_target_code=F('currency_target__currency_code'))

    def currency_base_code(self, obj):
        return obj.currency_base_code

    def currency_target_code(self, obj):
        return obj.currency_target_code

    currency_base_code.admin_order_field = 'currency_base__currency_code'
    currency_base_code.short_description = 'Currency Base Code'

    currency_target_code.admin_order_field = 'currency_target__currency_code'
    currency_target_code.short_description = 'Currency Target Code'

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj:
            defaults.update({'form': CurrencyRateForm})
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def has_change_permission(self, request, obj=None):
        return False
