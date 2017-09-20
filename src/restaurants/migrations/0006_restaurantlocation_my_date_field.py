# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20170831_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='my_date_field',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
