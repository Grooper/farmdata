from rest_framework import serializers

from ..models import Harvest


class HarvestSerializer(serializers.ModelSerializer):
    """
    Harvest Model Serializer
    """
    class Meta:
        model = Harvest

        fields = (
            'id',
            'date',
            'amount',
            'hours',
            'gen',
            'comments',
            'user',
            'field',
            'crop',
            'unit',
        )

        read_only_fields = ('date',)
