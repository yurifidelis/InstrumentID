# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_wmid', '0003_remove_track_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='file',
            field=models.FileField(null=True, upload_to=b'uploads'),
        ),
    ]
