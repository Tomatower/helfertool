# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_event_changes_until'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='deposit',
            field=models.BooleanField(default=False, verbose_name='A deposit has to be made to receive the gifts.'),
        ),
    ]
