# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-25 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='昵称')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='手机号')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/photo', verbose_name='用户头像')),
                ('real_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='真实姓名')),
                ('image_forward', models.ImageField(blank=True, null=True, upload_to='users/photo', verbose_name='身份正面照片')),
                ('image_back', models.ImageField(blank=True, null=True, upload_to='users/photo', verbose_name='身份反面照片')),
                ('card', models.CharField(blank=True, max_length=20, null=True, verbose_name='身份证号码')),
            ],
            options={
                'verbose_name': '用户详情',
                'verbose_name_plural': '用户详情',
                'db_table': 'app_user_profile',
            },
        ),
        migrations.AddField(
            model_name='loginuser',
            name='is_activated',
            field=models.BooleanField(default=False, verbose_name='是否激活'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.LoginUser', verbose_name='用户ID'),
        ),
    ]
