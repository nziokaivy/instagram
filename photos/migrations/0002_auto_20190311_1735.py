# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-11 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_bio',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
