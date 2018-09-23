# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrecord',
            name='operator',
            field=models.CharField(default='', max_length=64, verbose_name='\u8bb0\u5f55\u4eba'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workrecord',
            name='record_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 23, 15, 24, 0, 970811), verbose_name='\u4f1a\u8bae\u65f6\u95f4'),
        ),
    ]
