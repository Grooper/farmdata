from django.db import models


class ConfigurationManager(models.Manager):
    """
    Configuration Manager
    """
    pass


class Configuration(models.Model):
    """
    Configuration Model
    """
    notes = models.BooleanField(blank=True, default=True)
    labor = models.BooleanField(blank=True, default=True)
    seed_order = models.BooleanField(blank=True, default=True)
    harv_list = models.BooleanField(blank=True, default=True)
    soil = models.BooleanField(blank=True, default=True)
    fertility = models.BooleanField(blank=True, default=True)
    cover = models.BooleanField(blank=True, default=True)
    compost = models.BooleanField(blank=True, default=True)
    fertilizer = models.BooleanField(blank=True, default=True)
    liquid_fertilizer = models.BooleanField(blank=True, default=True)
    dry_fertilizer = models.BooleanField(blank=True, default=True)
    tillage = models.BooleanField(blank=True, default=True)
    spraying = models.BooleanField(blank=True, default=True)
    back_spray = models.BooleanField(blank=True, default=True)
    tractor_spray = models.BooleanField(blank=True, default=True)
    scouting = models.BooleanField(blank=True, default=True)
    insect = models.BooleanField(blank=True, default=True)
    weed = models.BooleanField(blank=True, default=True)
    disease = models.BooleanField(blank=True, default=True)
    irrigation = models.BooleanField(blank=True, default=True)
    pump = models.BooleanField(blank=True, default=True)
    sales = models.BooleanField(blank=True, default=True)
    sales_packing = models.BooleanField(blank=True, default=True)
    sales_invoice = models.BooleanField(blank=True, default=True)
    bedft = models.BooleanField(blank=True, default=True)
    gens = models.BooleanField(blank=True, default=True)

    num_top = models.IntegerField(blank=True, null=True)
    num_harvest = models.IntegerField(blank=True, null=True)
    num_soil = models.IntegerField(blank=True, null=True)
    num_fertility = models.IntegerField(blank=True, null=True)
    num_fertilizer = models.IntegerField(blank=True, null=True)
    num_spray = models.IntegerField(blank=True, null=True)
    num_scout = models.IntegerField(blank=True, null=True)
    num_admin = models.IntegerField(blank=True, null=True)
    num_add = models.IntegerField(blank=True, null=True)
    num_add_crop = models.IntegerField(blank=True, null=True)
    num_add_equip = models.IntegerField(blank=True, null=True)
    num_add_soil = models.IntegerField(blank=True, null=True)
    num_add_species = models.IntegerField(blank=True, null=True)
    num_add_other = models.IntegerField(blank=True, null=True)
    num_edit = models.IntegerField(blank=True, null=True)
    num_edit_soil = models.IntegerField(blank=True, null=True)
    num_edit_soil_fertility = models.IntegerField(blank=True, null=True)
    num_edit_soil_material = models.IntegerField(blank=True, null=True)
    num_edit_other = models.IntegerField(blank=True, null=True)
    num_view_graphs = models.IntegerField(blank=True, null=True)
    num_sales = models.IntegerField(blank=True, null=True)
    num_add_sales = models.IntegerField(blank=True, null=True)
    num_edit_sales = models.IntegerField(blank=True, null=True)

    farm = models.OneToOneField('core.Farm', related_name='configuration')

    objects = ConfigurationManager()
