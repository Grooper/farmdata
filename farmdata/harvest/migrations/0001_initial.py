# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('amount', models.FloatField()),
                ('hours', models.FloatField(default=0, null=True, blank=True)),
                ('gen', models.IntegerField(default=1, null=True, blank=True)),
                ('comments', models.TextField(default=b'', null=True, blank=True)),
                ('crop', models.ForeignKey(related_name='harvests', to='core.Crop')),
                ('field', models.ForeignKey(related_name='harvests', to='core.Field')),
                ('unit', models.ForeignKey(related_name='harvests', to='core.Unit')),
                ('user', models.ForeignKey(related_name='harvests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
