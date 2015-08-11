# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_wmid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='file',
            field=models.FileField(null=True, upload_to=b'uploads'),
        ),
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
