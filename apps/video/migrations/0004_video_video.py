# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-10 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20180327_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(default='', upload_to='videos/%Y/%m', verbose_name='\u89c6\u9891\u4e0a\u4f20'),
        ),
    ]
