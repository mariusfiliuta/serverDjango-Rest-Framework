# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-08 18:52
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileApi', '0007_auto_20170408_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='image_paths',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None),
        ),
    ]
