# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 17:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0030_auto_20180126_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliates',
            name='prospects',
            field=models.ManyToManyField(related_name='Prospects', to=settings.AUTH_USER_MODEL),
        ),
    ]