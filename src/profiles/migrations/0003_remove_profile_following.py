# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170921_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
    ]
