# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_capacity', '0002_auto_20181002_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capacitydata',
            old_name='use',
            new_name='used',
        ),
    ]
