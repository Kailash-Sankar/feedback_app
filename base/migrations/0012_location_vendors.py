# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-05 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_category_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('active', models.BooleanField(default=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Location')),
            ],
        ),
    ]
