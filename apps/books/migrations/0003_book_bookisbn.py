# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-30 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20171228_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookISBN',
            field=models.CharField(default='', max_length=50),
        ),
    ]
