# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-01 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_answer_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Category'),
            preserve_default=False,
        ),
    ]
