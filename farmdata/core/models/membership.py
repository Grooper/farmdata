import random

from django.db import models


class MembershipManager(models.Manager):
    """
    Membership Manager
    """
    def create(self, *args, **kwargs):
        """
        Override create function
        """
        # Create new Membership
        membership = self.model(
            *args,
            **kwargs
        )

        # Save to database
        membership.save()

        # Return newly created object
        return membership


class Membership(models.Model):
    """
    Membership Model
    Map Users to Farms using a ManyToManyField
    Use an intermediary Many To Many Relation, defined through 'Membership'
    https://docs.djangoproject.com/en/1.8/topics/db/models/#intermediary-manytomany
    """
    MEMBER = 0
    ADMIN = 1
    MEMBERSHIP_STATUSES = (
        (MEMBER, 'member'),
        (ADMIN, 'admin'),
    )

    farm = models.ForeignKey('core.Farm', related_name='memberships')
    user = models.ForeignKey('core.User', related_name='memberships')
    membership_status = models.PositiveSmallIntegerField(choices=MEMBERSHIP_STATUSES, default=MEMBER)

    objects = MembershipManager()

    class Meta:
        unique_together = (('farm', 'user'))
