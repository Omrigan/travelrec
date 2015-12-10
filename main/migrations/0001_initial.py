# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TGcmRegId',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('reg_id', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('status', models.IntegerField()),
                ('parent_id', models.IntegerField()),
                ('lang', models.CharField(max_length=10)),
                ('device_model', models.CharField(max_length=500)),
                ('system_version', models.CharField(max_length=255)),
                ('app_version', models.CharField(max_length=255)),
                ('created', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 't_gcm_reg_id',
            },
        ),
        migrations.CreateModel(
            name='TGpsTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('time', models.DateTimeField()),
                ('speed', models.FloatField()),
                ('altitude', models.FloatField()),
                ('number', models.SmallIntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 't_gps_tracker',
            },
        ),
        migrations.CreateModel(
            name='THelps',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=125)),
                ('time', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_helps',
            },
        ),
        migrations.CreateModel(
            name='TMessages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('recipient_id', models.IntegerField()),
                ('sender_id', models.IntegerField()),
                ('text', models.CharField(max_length=1000)),
                ('read', models.IntegerField()),
                ('time_create', models.BigIntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 't_messages',
            },
        ),
        migrations.CreateModel(
            name='TNotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_id', models.IntegerField()),
                ('text', models.CharField(max_length=10000)),
                ('title', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('vk', models.IntegerField()),
                ('fb', models.IntegerField()),
                ('tw', models.IntegerField()),
                ('access', models.IntegerField()),
                ('date_update', models.DateTimeField()),
                ('time_create', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 't_notes',
            },
        ),
        migrations.CreateModel(
            name='TUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('user_email', models.CharField(max_length=255)),
                ('pass_field', models.CharField(max_length=255, db_column='pass')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('lasttime', models.DateTimeField()),
                ('status', models.CharField(max_length=125)),
                ('visible', models.IntegerField()),
                ('about', models.CharField(max_length=255)),
                ('photo50', models.CharField(max_length=255)),
                ('photo100', models.CharField(max_length=255)),
                ('photo200', models.CharField(max_length=255)),
                ('reg_ip', models.CharField(max_length=255)),
                ('from_city', models.CharField(max_length=25)),
                ('data_reg', models.DateTimeField()),
                ('birthday', models.DateField()),
                ('vkid', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('lang', models.CharField(max_length=50)),
                ('fbid', models.IntegerField()),
                ('time_trip', models.TimeField()),
                ('skype', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('jobs', models.CharField(max_length=250)),
                ('study', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 't_users',
            },
        ),
    ]
