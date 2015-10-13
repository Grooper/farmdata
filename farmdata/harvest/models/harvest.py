from datetime import datetime

from django.conf import settings
from django.db import models


class HarvestManager(models.Manager):
    """
    Harvest Manager
    """
    def create(self, *args, **kwargs):
        """
        Override create function
        """
        # Create new Membership
        harvest = self.model(
            *args,
            **kwargs
        )

        # If no date was specified, set the date to now
        if not harvest.date:
            harvest.date = datetime.now()

        # Save to database
        harvest.save()

        # Return newly created object
        return harvest


class Harvest(models.Model):
    """
    Harvest Model
    """
    date = models.DateField(blank=True)
    amount = models.FloatField()
    hours = models.FloatField(blank=True, null=True, default=0)
    gen = models.IntegerField(blank=True, null=True, default=1)
    comments = models.TextField(blank=True, null=True, default='')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='harvests')
    field = models.ForeignKey('core.Field', related_name='harvests')
    crop = models.ForeignKey('core.Crop', related_name='harvests')
    unit = models.ForeignKey('core.Unit', related_name='harvests')

    objects = HarvestManager()
