# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.BooleanField(default=True)),
                ('labor', models.BooleanField(default=True)),
                ('seed_order', models.BooleanField(default=True)),
                ('harv_list', models.BooleanField(default=True)),
                ('soil', models.BooleanField(default=True)),
                ('fertility', models.BooleanField(default=True)),
                ('cover', models.BooleanField(default=True)),
                ('compost', models.BooleanField(default=True)),
                ('fertilizer', models.BooleanField(default=True)),
                ('liquid_fertilizer', models.BooleanField(default=True)),
                ('dry_fertilizer', models.BooleanField(default=True)),
                ('tillage', models.BooleanField(default=True)),
                ('spraying', models.BooleanField(default=True)),
                ('back_spray', models.BooleanField(default=True)),
                ('tractor_spray', models.BooleanField(default=True)),
                ('scouting', models.BooleanField(default=True)),
                ('insect', models.BooleanField(default=True)),
                ('weed', models.BooleanField(default=True)),
                ('disease', models.BooleanField(default=True)),
                ('irrigation', models.BooleanField(default=True)),
                ('pump', models.BooleanField(default=True)),
                ('sales', models.BooleanField(default=True)),
                ('sales_packing', models.BooleanField(default=True)),
                ('sales_invoice', models.BooleanField(default=True)),
                ('bedft', models.BooleanField(default=True)),
                ('gens', models.BooleanField(default=True)),
                ('num_top', models.IntegerField(null=True, blank=True)),
                ('num_harvest', models.IntegerField(null=True, blank=True)),
                ('num_soil', models.IntegerField(null=True, blank=True)),
                ('num_fertility', models.IntegerField(null=True, blank=True)),
                ('num_fertilizer', models.IntegerField(null=True, blank=True)),
                ('num_spray', models.IntegerField(null=True, blank=True)),
                ('num_scout', models.IntegerField(null=True, blank=True)),
                ('num_admin', models.IntegerField(null=True, blank=True)),
                ('num_add', models.IntegerField(null=True, blank=True)),
                ('num_add_crop', models.IntegerField(null=True, blank=True)),
                ('num_add_equip', models.IntegerField(null=True, blank=True)),
                ('num_add_soil', models.IntegerField(null=True, blank=True)),
                ('num_add_species', models.IntegerField(null=True, blank=True)),
                ('num_add_other', models.IntegerField(null=True, blank=True)),
                ('num_edit', models.IntegerField(null=True, blank=True)),
                ('num_edit_soil', models.IntegerField(null=True, blank=True)),
                ('num_edit_soil_fertility', models.IntegerField(null=True, blank=True)),
                ('num_edit_soil_material', models.IntegerField(null=True, blank=True)),
                ('num_edit_other', models.IntegerField(null=True, blank=True)),
                ('num_view_graphs', models.IntegerField(null=True, blank=True)),
                ('num_sales', models.IntegerField(null=True, blank=True)),
                ('num_add_sales', models.IntegerField(null=True, blank=True)),
                ('num_edit_sales', models.IntegerField(null=True, blank=True)),
                ('farm', models.OneToOneField(related_name='configuration', to='core.Farm')),
            ],
        ),
    ]
