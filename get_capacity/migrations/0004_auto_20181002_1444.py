# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_capacity', '0003_auto_20181002_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacitydata',
            name='use',
            field=models.CharField(default='', max_length=64, verbose_name=b'Use%'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='capacitydata',
            name='used',
            field=models.CharField(max_length=64, verbose_name=b'used'),
        ),
    ]
