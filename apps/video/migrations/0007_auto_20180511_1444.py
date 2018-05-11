# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-11 14:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_auto_20180410_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='\u89c6\u9891\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.CharField(choices=[('cy', '1'), ('sh', '2'), ('qs', '3')], default=1, max_length=20, verbose_name='\u89c6\u9891\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='video',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='\u89c6\u9891\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_need',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='\u89c6\u9891\u987b\u77e5'),
        ),
    ]
