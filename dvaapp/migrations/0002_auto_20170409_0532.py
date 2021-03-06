# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlabel',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='vlabel',
            name='vdn_dataset',
        ),
        migrations.AlterUniqueTogether(
            name='vlabel',
            unique_together=set([('source', 'label_name', 'video')]),
        ),
    ]
