# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0002_auto_20170409_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlabel',
            name='vdn_dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.VDNDataset'),
        ),
    ]
