# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-01 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20170201_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='feedback',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Feedback'),
            preserve_default=False,
        ),
    ]
