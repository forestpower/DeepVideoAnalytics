# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexentries',
            name='vdn_key',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='indexentries',
            name='vdn_source',
            field=models.URLField(default=''),
        ),
    ]