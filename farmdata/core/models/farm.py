from django.conf import settings
from django.db import models
from django.contrib.auth.models import Group, GroupManager

from .membership import Membership

class FarmManager(GroupManager):
    """
    Farm Manager
    Extends django.contrib.auth.models.GroupManager
    """
    def create(self, *args, **kwargs):
        # Create new Farm
        group = self.model(
            *args,
            **kwargs
        )

        # Save to database
        group.save()

        # Create Membership relation between new Farm and Farm Owner
        group.add_member(group.owner)

        # Return newly created object
        return group


class Farm(Group):
    """
    Farm Model
    Extends django.contrib.auth.models.Group
    https://docs.djangoproject.com/en/1.8/ref/contrib/auth/#django.contrib.auth.models.Group
    """
    location = models.CharField(blank=True, null=True, max_length=255)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owned_groups')
    members = models.ManyToManyField('core.User', through='core.Membership', through_fields=('farm', 'user'), related_name='farms')

    objects = FarmManager()

    def add_member(self, user):
        """
        Add the given User to this Farm
        Update Farm status if necessary
        """
        # Create Membership relation
        membership_data = {
            'farm': self,
            'user': user,
        }
        Membership.objects.create(**membership_data)

    def remove_member(self, user):
        """
        Remove the given User from this Farm
        Update Farm status if necessary
        """
        # Delete Membership relation
        lookup_data = {
            'farm': self,
            'user': user,
        }
        Membership.objects.get(**lookup_data).delete()
