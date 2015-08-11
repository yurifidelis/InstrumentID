# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_wmid', '0003_auto_20150809_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='coverURL',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
