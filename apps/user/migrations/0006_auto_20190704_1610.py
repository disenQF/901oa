# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_uservideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservideo',
            name='video_poster',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='视频封面图片'),
        ),
    ]
