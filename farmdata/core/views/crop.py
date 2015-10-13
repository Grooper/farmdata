from rest_framework import viewsets

from ..models import Crop, Unit, UnitConversion
from ..serializers import CropSerializer, UnitSerializer, UnitConversionSerializer


class CropViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `Crop` Model
    """
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    filter_fields = ()


class UnitViewSet(viewsets.ModelViewSet):
	"""
	Endpoint for `Unit` Model
	"""
	queryset = Unit.objects.all()
	serializer_class = UnitSerializer
	filter_fields = ()


class UnitConversionViewSet(viewsets.ModelViewSet):
	"""
	Endpoint for `UnitConversion` Model
	"""
	queryset = UnitConversion.objects.all()
	serializer_class = UnitConversionSerializer
	filter_fields = ()
