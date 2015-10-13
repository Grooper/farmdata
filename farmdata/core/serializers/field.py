from rest_framework import serializers

from ..models import Field


class FieldSerializer(serializers.ModelSerializer):
    """
    Field Model Serializer
    """
    class Meta:
        model = Field

        fields = (
            'id',
            'name',
            'size',
            'number_of_beds',
            'length',
            'active',
        )
