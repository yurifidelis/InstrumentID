# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_wmid', '0002_auto_20151205_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='file',
        ),
    ]
