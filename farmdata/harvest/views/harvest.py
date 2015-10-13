from rest_framework import viewsets

from ..models import Harvest
from ..serializers import HarvestSerializer


class HarvestViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `Harvest` Model
    """
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer
    filter_fields = ()
