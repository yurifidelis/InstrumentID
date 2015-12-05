# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_wmid', '0002_auto_20151205_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='file',
        ),
        migrations.AddField(
            model_name='instrument',
            name='file',
            field=models.FileField(null=True, upload_to=b'uploads'),
        ),
    ]
