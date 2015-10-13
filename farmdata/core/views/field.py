from rest_framework import viewsets

from ..models import Field
from ..serializers import FieldSerializer


class FieldViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `Field` Model
    """
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    filter_fields = ()
