# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0003_auto_20160516_1551'),
        ('registration', '0009_event_gifts'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='gifts',
            field=models.ManyToManyField(blank=True, to='gifts.GiftSet', verbose_name='Gifts'),
        ),
    ]
