# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-28 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storeadmin',
            old_name='password',
            new_name='adminPassword',
        ),
    ]
