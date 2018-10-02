# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iwork', '0006_auto_20181002_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrecord',
            name='record_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 14, 43, 5, 586447), verbose_name='\u4f1a\u8bae\u65f6\u95f4'),
        ),
    ]
