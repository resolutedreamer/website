# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='address_one',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='address_two',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='city',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='state',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='stripe_id',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
