# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='dummy',
            field=models.CharField(default='', max_length=20),
        ),
    ]
