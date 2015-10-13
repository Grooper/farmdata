from rest_framework import status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from ..models import Farm
from ..serializers import FarmSerializer


class FarmViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `Farm` Model
    """
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    filter_fields = ('owner',)

    def perform_create(self, serializer):
        """
        Create hook
        The owner of the farm is specified to be the currently logged in user.
        """
        user = self.request.user
        serializer.save(owner=user)
        return Response({}, status=status.HTTP_201_CREATED)

    @detail_route(methods=['post'], url_path='join-farm')
    def join_farm(self, request, pk):
        """
        `/farms/{pk}/join-farm/`
        Add the currently logged in `User` to this `Farm`.
        """
        farm = self.get_object()
        user = request.user
        farm.add_member(user)
        return Response({}, status=status.HTTP_202_ACCEPTED)

    @detail_route(methods=['delete'], url_path='leave-farm')
    def leave_farm(self, request, pk):
        """
        `/farms/{pk}/leave-farm/`
        Remove the currently logged in `User` from this `Farm`.
        """
        farm = self.get_object()
        user = request.user
        farm.remove_member(user)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['post'], url_path='add-member')
    def add_member(self, request, pk):
        """
        `/farms/{pk]/add-member/`
        Invite the specified `User` to join this `Farm`.
        """
        farm = self.get_object()
        user = request.data.get('user')
        farm.add_member(user)
        return Response({}, status=status.HTTP_202_ACCEPTED)

    @detail_route(methods=['delete'], url_path='remove-member')
    def remove_member(self, request, pk):
        """
        `/farms/{pk}/remove-member/`
        Remove the specified `User` from this `Farm`.
        """
        farm = self.get_object()
        user = request.data.get('user')
        farm.remove_member(user)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
