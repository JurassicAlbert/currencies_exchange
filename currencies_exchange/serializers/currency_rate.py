from ..models.currency_rate import CurrencyRate
from rest_framework import serializers
from ..settings import DATETIME_FORMAT


class CurrencyRateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    currency_base = serializers.CharField()
    currency_target = serializers.CharField()
    rate = serializers.FloatField()
    history_date = serializers.DateTimeField(format=DATETIME_FORMAT)

    def create(self, validated_data):
        """
        Create and return a new `Currency` instance, given the validated data.
        """
        return CurrencyRate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Currency` instance, given the validated data.
        """
        instance.currency_base = validated_data.get('currency_base', instance.currency_base)
        instance.currency_target = validated_data.get('currency_target', instance.currency_target)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.history_date = validated_data.get('history_date', instance.history_date)
        instance.save()
        return instance

    class Meta:
        model = CurrencyRate
        fields = ['currency_base', 'currency_target', 'rate', 'history_date']
