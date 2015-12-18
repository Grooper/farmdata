from rest_framework import viewsets

from ..models import Configuration
from ..serializers import ConfigurationSerializer


class ConfigurationViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `Configuration` Model
    """
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
    filter_fields = ()
