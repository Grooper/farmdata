from rest_framework import serializers

from ..models import Crop, Unit, UnitConversion


class CropSerializer(serializers.ModelSerializer):
    """
    Crop Model Serializer
    """
    class Meta:
        model = Crop

        fields = (
            'id',
            'name',
            'active',
            'default_unit',
        )


class UnitSerializer(serializers.ModelSerializer):
    """
    Unit Model Serializer
    """
    class Meta:
        model = Unit

        fields = (
            'id',
            'name',
        )


class UnitConversionSerializer(serializers.ModelSerializer):
    """
    Unit Conversion Model Serializer
    """
    default_unit = serializers.SerializerMethodField()

    def get_default_unit(self, obj):
        """
        Get the default unit for this crop
        """
        return obj.crop.default_unit.id

    class Meta:
        model = UnitConversion

        fields = (
            'id',
            'active',
            'crop',
            'unit',
            'default_unit',
        )
