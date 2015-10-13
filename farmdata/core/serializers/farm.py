from rest_framework import serializers

from ..models import Farm


class FarmSerializer(serializers.ModelSerializer):
    """
    Farm Model Serializer
    """
    class Meta:
        model = Farm

        fields = (
            'id',
            'name',
            'location',
            'owner',
        )
