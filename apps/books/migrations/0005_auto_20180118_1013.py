# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20180107_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookAuthorIntroduction',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookIntroduction',
            field=models.CharField(default='', max_length=1000),
        ),
    ]