# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobileApi', '0002_auto_20170322_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Play_Representation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('actors', models.ManyToManyField(related_name='play_representations', to='mobileApi.Actor')),
            ],
        ),
        migrations.RemoveField(
            model_name='plays_representation',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='plays_representation',
            name='play',
        ),
        migrations.RemoveField(
            model_name='plays_representation',
            name='theater',
        ),
        migrations.RenameField(
            model_name='theater',
            old_name='location_latitude',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='theater',
            old_name='location_longitude',
            new_name='longitude',
        ),
        migrations.AlterField(
            model_name='comment',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mobileApi.Play'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mobileApi.User'),
        ),
        migrations.AlterField(
            model_name='play',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plays', to='mobileApi.Category'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='mobileApi.Play'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='mobileApi.User'),
        ),
        migrations.DeleteModel(
            name='Plays_Representation',
        ),
        migrations.AddField(
            model_name='play_representation',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='play_representations', to='mobileApi.Play'),
        ),
        migrations.AddField(
            model_name='play_representation',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='play_representations', to='mobileApi.Theater'),
        ),
    ]
