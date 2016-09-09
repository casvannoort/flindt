# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 15:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0005_auto_20160906_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='purpose',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]