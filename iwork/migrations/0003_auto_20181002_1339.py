# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iwork', '0002_auto_20180923_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrecord',
            name='record_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 13, 39, 52, 193592), verbose_name='\u4f1a\u8bae\u65f6\u95f4'),
        ),
    ]
