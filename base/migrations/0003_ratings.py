# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-31 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_category_ico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ico_name', models.CharField(max_length=80)),
            ],
        ),
    ]
