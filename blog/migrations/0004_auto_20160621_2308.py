# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160621_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='startups',
            field=models.ManyToManyField(to='organizer.Startup'),
        ),
    ]
