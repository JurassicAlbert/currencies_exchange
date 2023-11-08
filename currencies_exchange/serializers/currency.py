from ..models.currency import Currency
from rest_framework import serializers


class CurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    currency_name = serializers.CharField()
    currency_symbol = serializers.CharField()
    currency_code = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Currency` instance, given the validated data.
        """
        return Currency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Currency` instance, given the validated data.
        """
        instance.currency_name = validated_data.get('currency_name', instance.currency_name)
        instance.currency_symbol = validated_data.get('currency_symbol', instance.currency_symbol)
        instance.currency_code = validated_data.get('currency_code', instance.currency_code)
        instance.save()
        return instance

    class Meta:
        model = Currency
        fields = ['currency_name', 'currency_symbol', 'currency_code']
