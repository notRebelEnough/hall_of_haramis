# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-10 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # migrations.CreateModel(
        #     name='tweets',
        #     fields=[
        #         ('id', models.AutoField(primary_key=True, serialize=False)),
        #         ('data_tweet_id', models.BigIntegerField()),
        #         ('data_user_id', models.CharField(max_length=255)),
        #         ('data_permalink_path', models.CharField(max_length=255)),
        #         ('data_screen_name', models.CharField(max_length=255)),
        #         ('data_you_follow', models.BooleanField(default=False)),
        #         ('data_follow_you', models.BooleanField(default=False)),
        #         ('tweet_text', models.CharField(max_length=128)),
        #         ('machine_label', models.CharField(default=None, max_length=128)),
        #         ('human_label', models.CharField(blank=True, max_length=128)),
        #         ('confidence', models.IntegerField(default=None)),
        #         ('created_at', models.DateTimeField(auto_now_add=True)),
        #         ('updated_at', models.DateTimeField(auto_now=True)),
        #     ],
        #     options={
        #         'db_table': 'tweets',
        #     },
        # ),
    ]