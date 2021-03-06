# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 07:22
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(upload_to='images/actors/profilePictures/')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('image_paths', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='images/plays/'), size=None)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApi.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Plays_Representation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_stage_at', models.DateTimeField()),
                ('actors', models.ManyToManyField(to='mobileApi.Actor')),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApi.Play')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_number', models.IntegerField(default=0)),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApi.Play')),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(upload_to='images/users/profilePictures/')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApi.User'),
        ),
        migrations.AddField(
            model_name='plays_representation',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApi.Theater'),
        ),
        migrations.AddField(
            model_name='comment',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApi.Play'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileApi.User'),
        ),
    ]
