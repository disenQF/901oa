# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190626_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=200, verbose_name='视频下载')),
                ('title', models.CharField(max_length=200, verbose_name='视频标题')),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容简介')),
                ('video_poster', models.CharField(max_length=100, verbose_name='视频封面图片')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.LoginUser', verbose_name='用户名')),
            ],
            options={
                'verbose_name': '用户视频',
                'verbose_name_plural': '用户视频',
                'db_table': 'app_user_video',
            },
        ),
    ]
