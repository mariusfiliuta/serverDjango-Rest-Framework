# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-09 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileApi', '0008_auto_20170408_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='image_paths',
            field=models.CharField(max_length=255),
        ),
    ]
