# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-20 06:57
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180820_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326),
        ),
    ]