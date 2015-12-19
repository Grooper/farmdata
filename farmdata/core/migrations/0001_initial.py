# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import farmdata.core.models.farm
import farmdata.core.models.user
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('jwt_secret_key', models.CharField(default=farmdata.core.models.user._generate_jwt_secret_key, max_length=30, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('signature', models.TextField(null=True, blank=True)),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', farmdata.core.models.farm.FarmManager()),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('size', models.FloatField()),
                ('number_of_beds', models.FloatField(null=True, blank=True)),
                ('length', models.FloatField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('membership_status', models.PositiveSmallIntegerField(default=0, choices=[(0, b'member'), (1, b'admin')])),
                ('farm', models.ForeignKey(related_name='memberships', to='core.Farm')),
                ('user', models.ForeignKey(related_name='memberships', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UnitConversion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('conversion', models.FloatField()),
                ('crop', models.ForeignKey(related_name='unit_conversions', to='core.Crop')),
                ('unit', models.ForeignKey(related_name='unit_conversions', to='core.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='farm',
            name='members',
            field=models.ManyToManyField(related_name='farms', through='core.Membership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='farm',
            name='owner',
            field=models.ForeignKey(related_name='owned_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='crop',
            name='default_unit',
            field=models.ForeignKey(related_name='units', to='core.Unit'),
        ),
        migrations.AlterUniqueTogether(
            name='unitconversion',
            unique_together=set([('crop', 'unit')]),
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('farm', 'user')]),
        ),
    ]
