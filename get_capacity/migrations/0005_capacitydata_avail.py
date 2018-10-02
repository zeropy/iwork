# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_capacity', '0004_auto_20181002_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacitydata',
            name='avail',
            field=models.CharField(default='', max_length=64, verbose_name=b'avail'),
            preserve_default=False,
        ),
    ]
