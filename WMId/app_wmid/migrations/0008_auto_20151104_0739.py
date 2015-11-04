# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    dependencies = [
        ('app_wmid', '0007_auto_20150817_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=durationfield.db.models.fields.duration.DurationField(),
        ),
    ]
