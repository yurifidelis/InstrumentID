# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('year', models.IntegerField()),
                ('coverURL', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=b'uploads')),
                ('title', models.CharField(max_length=255)),
                ('position', models.IntegerField()),
                ('duration', durationfield.db.models.fields.duration.DurationField()),
                ('is_instrumental', models.BooleanField(default=False)),
                ('album', models.ForeignKey(to='app_wmid.Album')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('created_time', models.DateTimeField(editable=False)),
                ('modified_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserLibrary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album', models.ForeignKey(to='app_wmid.Album')),
                ('user', models.ForeignKey(to='app_wmid.User')),
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='instrument_class',
            field=models.ForeignKey(to='app_wmid.InstrumentClass'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='track',
            field=models.ForeignKey(to='app_wmid.Track'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='app_wmid.Artist'),
        ),
    ]
