# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0004_auto_20181010_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panfile',
            name='filepath',
        ),
        migrations.AddField(
            model_name='panfile',
            name='userpath',
            field=models.CharField(default='', max_length=256, verbose_name='\u7528\u6237\u81ea\u5b9a\u4e49\u8def\u5f84'),
        ),
    ]