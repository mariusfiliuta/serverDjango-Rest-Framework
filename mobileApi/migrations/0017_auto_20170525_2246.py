# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-25 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileApi', '0016_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
    ]
