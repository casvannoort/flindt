# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('rating', models.ManyToManyField(blank=True, to='feedback.Rating')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
