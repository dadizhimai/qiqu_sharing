# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-26 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='teacher_tell',
            new_name='relevant_tell',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='course_need',
            new_name='video_need',
        ),
    ]