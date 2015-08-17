# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_wmid', '0005_auto_20150809_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='is_instrumental',
            field=models.BooleanField(default=False),
        ),
    ]
