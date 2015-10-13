from django.db import models


class CropManager(models.Manager):
    """
    Crop Manager
    """
    pass


class Crop(models.Model):
    """
    Crop Model
    """
    name = models.CharField(unique=True, max_length=255)
    active = models.BooleanField(blank=True, default=True)

    default_unit = models.ForeignKey('core.Unit', related_name='units')

    objects = CropManager()


class UnitManager(models.Manager):
    """
    Unit Manager
    """
    pass


class Unit(models.Model):
    """
    Unit Model
    """
    name = models.CharField(unique=True, max_length=255)

    objects = UnitManager()


class UnitConversionManager(models.Manager):
    """
    Unit Conversion Manager
    """
    pass


class UnitConversion(models.Model):
    """
    Unit Conversion Model
    """
    active = models.BooleanField(blank=True, default=True)
    conversion = models.FloatField()

    crop = models.ForeignKey('core.Crop', related_name='unit_conversions')
    unit = models.ForeignKey('core.Unit', related_name='unit_conversions')

    objects = UnitConversionManager()

    class Meta:
        unique_together = (('crop', 'unit'))
