# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0003_auto_20160621_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslink',
            name='startup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.Startup'),
        ),
    ]
