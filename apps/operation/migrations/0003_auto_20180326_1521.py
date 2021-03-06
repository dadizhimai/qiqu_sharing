# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-26 15:21
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0001_initial'),
        ('operation', '0002_auto_20180326_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video', verbose_name='\u89c6\u9891')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u89c6\u9891',
                'verbose_name_plural': '\u7528\u6237\u89c6\u9891',
            },
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='course',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserCourse',
        ),
    ]
