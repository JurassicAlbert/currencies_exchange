from rest_framework import serializers
from ..settings import DATETIME_FORMAT
from ..models.currency_rate import CurrencyRate


class CurrencyRateSerializer(serializers.Serializer):
    """
    Serializer for the CurrencyRate model.

    This serializer defines the fields and methods for serializing and deserializing
    CurrencyRate instances.

    Attributes:
        id (serializers.IntegerField): The ID of the currency rate (read-only).
        currency_base (serializers.CharField): The base currency code.
        currency_target (serializers.CharField): The target currency code.
        rate (serializers.FloatField): The exchange rate.
        history_date (serializers.DateTimeField): The date of the exchange rate.

    Methods:
        create(validated_data): Create and return a new CurrencyRate instance.
        update(instance, validated_data): Update and return an existing CurrencyRate instance.

    Meta:
        model (CurrencyRate): The model associated with the serializer.
        fields (list): The list of fields to be included in the serialized representation.

    Example:
        To serialize a CurrencyRate instance:
        serializer = CurrencyRateSerializer(data=data)
        serializer.is_valid()
        serialized_data = serializer.data
    """

    id = serializers.IntegerField(read_only=True)
    currency_base = serializers.CharField()
    currency_target = serializers.CharField()
    rate = serializers.FloatField()
    history_date = serializers.DateTimeField(format=DATETIME_FORMAT)

    def create(self, validated_data):
        """
        Create and return a new `CurrencyRate` instance, given the validated data.

        Args:
            validated_data (dict): The validated data to create a new instance.

        Returns:
            CurrencyRate: The newly created CurrencyRate instance.
        """
        return CurrencyRate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `CurrencyRate` instance, given the validated data.

        Args:
            instance (CurrencyRate): The existing CurrencyRate instance to be updated.
            validated_data (dict): The validated data for updating the instance.

        Returns:
            CurrencyRate: The updated CurrencyRate instance.
        """
        instance.currency_base = validated_data.get('currency_base', instance.currency_base)
        instance.currency_target = validated_data.get('currency_target', instance.currency_target)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.history_date = validated_data.get('history_date', instance.history_date)
        instance.save()
        return instance

    class Meta:
        """
        Metadata class for the CurrencyRateSerializer.

        Attributes:
            model (CurrencyRate): The model associated with the serializer.
            fields (list): The list of fields to be included in the serialized representation.
        """
        model = CurrencyRate
        fields = ['currency_base', 'currency_target', 'rate', 'history_date']
