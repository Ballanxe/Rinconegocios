# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-02 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0004_auto_20180201_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedeals',
            name='closed',
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='buy_is_finished',
            field=models.BooleanField(default=False, verbose_name='Did you buy this service ?'),
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='buyer_is_contacted',
            field=models.BooleanField(default=False, verbose_name='Did the company make contact with you ?'),
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='buyer_message',
            field=models.TextField(blank=True, null=True, verbose_name='Tell us what was your experience with this service?'),
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='created',
            field=models.DateTimeField(editable=False, null=True, verbose_name='creation date and time'),
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='This means that de deal was successful'),
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='modified',
            field=models.DateTimeField(null=True, verbose_name='modification date and time'),
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='sell_is_finished',
            field=models.BooleanField(default=False, verbose_name='Did you sell this service ?'),
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='seller_has_contacted',
            field=models.BooleanField(default=False, verbose_name='Have you already made contact with this client ?'),
        ),
        migrations.AddField(
            model_name='servicedeals',
            name='seller_message',
            field=models.TextField(blank=True, null=True, verbose_name='What do you want to say about this client?'),
        ),
    ]