# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 01:35
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20180204_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='serv_desc_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='English Service Description'),
        ),
    ]
