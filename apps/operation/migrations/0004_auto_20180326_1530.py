# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-26 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20180326_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userask',
            old_name='course_name',
            new_name='video_name',
        ),
    ]
