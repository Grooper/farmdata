from django.db import models


class FieldManager(models.Manager):
    """
    Field Manager
    """
    pass


class Field(models.Model):
    """
    Field Model
    """
    name = models.CharField(unique=True, max_length=255)
    size = models.FloatField()
    number_of_beds = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    active = models.BooleanField(blank=True, default=True)

    objects = FieldManager()
