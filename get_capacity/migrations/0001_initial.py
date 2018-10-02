# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapacityData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=64, null=True, verbose_name=b'ip', blank=True)),
                ('filesystem', models.CharField(max_length=64, verbose_name=b'filesystem')),
                ('size', models.CharField(max_length=64, verbose_name=b'size')),
                ('used', models.CharField(max_length=64, verbose_name=b'avail')),
                ('mounted', models.TextField(max_length=64, verbose_name=b'mounted')),
                ('createtime', models.DateTimeField(verbose_name='\u4fdd\u5b58\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u78c1\u76d8\u5bb9\u91cf\u6570\u636e',
                'verbose_name_plural': '\u78c1\u76d8\u5bb9\u91cf\u6570\u636e',
            },
        ),
    ]
