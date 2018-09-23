# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='workRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme', models.CharField(max_length=64, verbose_name='\u4f1a\u8bae\u4e3b\u9898')),
                ('content', models.CharField(max_length=1024, null=True, verbose_name='\u4f1a\u8bae\u5185\u5bb9', blank=True)),
                ('record_time', models.DateTimeField(default=datetime.datetime(2018, 9, 23, 15, 2, 5, 500501), verbose_name='\u4f1a\u8bae\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4f1a\u8bae\u8bb0\u5f55',
                'verbose_name_plural': '\u4f1a\u8bae\u8bb0\u5f55',
            },
        ),
    ]
