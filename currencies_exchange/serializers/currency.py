from ..models.currency import Currency
from rest_framework import serializers


class CurrencySerializer(serializers.Serializer):
    """
    Serializer for the Currency model.

    This serializer defines the fields and methods for serializing and deserializing
    Currency instances.

    Attributes:
        id (serializers.IntegerField): The ID of the currency (read-only).
        currency_name (serializers.CharField): The name of the currency.
        currency_symbol (serializers.CharField): The symbol of the currency.
        currency_code (serializers.CharField): The code of the currency.

    Methods:
        create(validated_data): Create and return a new Currency instance.
        update(instance, validated_data): Update and return an existing Currency instance.

    Meta:
        model (Currency): The model associated with the serializer.
        fields (list): The list of fields to be included in the serialized representation.

    Example:
        To serialize a Currency instance:
        serializer = CurrencySerializer(data=data)
        serializer.is_valid()
        serialized_data = serializer.data
    """

    id = serializers.IntegerField(read_only=True)
    currency_name = serializers.CharField()
    currency_symbol = serializers.CharField()
    currency_code = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Currency` instance, given the validated data.

        Args:
            validated_data (dict): The validated data to create a new instance.

        Returns:
            Currency: The newly created Currency instance.
        """
        return Currency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Currency` instance, given the validated data.

        Args:
            instance (Currency): The existing Currency instance to be updated.
            validated_data (dict): The validated data for updating the instance.

        Returns:
            Currency: The updated Currency instance.
        """
        instance.currency_name = validated_data.get('currency_name', instance.currency_name)
        instance.currency_symbol = validated_data.get('currency_symbol', instance.currency_symbol)
        instance.currency_code = validated_data.get('currency_code', instance.currency_code)
        instance.save()
        return instance

    class Meta:
        """
        Metadata class for the CurrencySerializer.

        Attributes:
            model (Currency): The model associated with the serializer.
            fields (list): The list of fields to be included in the serialized representation.
        """
        model = Currency
        fields = ['currency_name', 'currency_symbol', 'currency_code']
