# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 09:22
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0005_feedbackonindividual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 'Incomplete'), (1, 'Complete')], default=0)),
                ('how_recognizable', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('how_valuable', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('actionable', models.BooleanField()),
                ('actionable_content', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeedbackOnRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='feedbackonindividual',
            name='actionable',
        ),
        migrations.RemoveField(
            model_name='feedbackonindividual',
            name='actionable_content',
        ),
        migrations.RemoveField(
            model_name='feedbackonindividual',
            name='date',
        ),
        migrations.RemoveField(
            model_name='feedbackonindividual',
            name='how_recognizable',
        ),
        migrations.RemoveField(
            model_name='feedbackonindividual',
            name='how_valuable',
        ),
        migrations.RemoveField(
            model_name='feedbackonindividual',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='feedbackonindividual',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='feedbackonindividual',
            name='status',
        ),
        migrations.AddField(
            model_name='feedback',
            name='individual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.FeedbackOnIndividual'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_received_feedback', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.FeedbackOnRole'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_sent_feedback', to=settings.AUTH_USER_MODEL),
        ),
    ]