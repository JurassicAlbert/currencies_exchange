from django.contrib import admin

from .models import Currency, CurrencyRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    search_fields = ['currency_name', 'currency_code']
    list_display = ['id', 'currency_name', 'currency_symbol', 'currency_code']
    list_filter = ['id', 'currency_name', 'currency_symbol', 'currency_code']
    list_per_page = 10

    def has_add_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(CurrencyRate)
class CurrencyAdmin(admin.ModelAdmin):
    search_fields = ['currency_base', 'currency_target']
    list_display = ['id', 'currency_base', 'currency_target', 'rate', 'history_date']
    list_filter = ['id', 'currency_base', 'currency_target', 'rate', 'history_date']
    list_per_page = 10

    def has_add_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False
