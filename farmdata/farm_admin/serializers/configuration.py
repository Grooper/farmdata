from rest_framework import serializers

from ..models import Configuration


class ConfigurationSerializer(serializers.ModelSerializer):
    """
    Configuration Model Serializer
    """
    class Meta:
        model = Configuration

        fields = (
            'id',
            
            'notes',
            'labor',
            'seed_order',
            'harv_list',
            'soil',
            'fertility',
            'cover',
            'compost',
            'fertilizer',
            'liquid_fertilizer',
            'dry_fertilizer',
            'tillage',
            'spraying',
            'back_spray',
            'tractor_spray',
            'scouting',
            'insect',
            'weed',
            'disease',
            'irrigation',
            'pump',
            'sales',
            'sales_packing',
            'sales_invoice',
            'bedft',
            'gens',

            'num_top',
            'num_harvest',
            'num_soil',
            'num_fertility',
            'num_fertilizer',
            'num_spray',
            'num_scout',
            'num_admin',
            'num_add',
            'num_add_crop',
            'num_add_equip',
            'num_add_soil',
            'num_add_species',
            'num_add_other',
            'num_edit',
            'num_edit_soil',
            'num_edit_soil_fertility',
            'num_edit_soil_material',
            'num_edit_other',
            'num_view_graphs',
            'num_sales',
            'num_add_sales',
            'num_edit_sales',

            'farm',
        )
        read_only_fields = ('farm',)            
