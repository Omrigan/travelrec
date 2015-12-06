# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class TGcmRegId(models.Model):
    reg_id = models.CharField(max_length=255)
    user_id = models.IntegerField()
    status = models.IntegerField()
    parent_id = models.IntegerField()
    lang = models.CharField(max_length=10)
    device_model = models.CharField(max_length=500)
    system_version = models.CharField(max_length=255)
    app_version = models.CharField(max_length=255)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_gcm_reg_id'


class TGpsTracker(models.Model):
    user = models.ForeignKey('TUsers')
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateTimeField()
    speed = models.FloatField()
    altitude = models.FloatField()
    number = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 't_gps_tracker'


class THelps(models.Model):
    user_id = models.IntegerField(primary_key=True)
    message = models.CharField(max_length=125)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_helps'


class TMessages(models.Model):
    recipient_id = models.IntegerField()
    sender_id = models.IntegerField()
    text = models.CharField(max_length=1000)
    read = models.IntegerField()
    time_create = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 't_messages'


class TNotes(models.Model):
    user_id = models.IntegerField()
    text = models.CharField(max_length=920)
    title = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    vk = models.IntegerField()
    fb = models.IntegerField()
    tw = models.IntegerField()
    access = models.IntegerField()
    date_update = models.DateTimeField()
    time_create = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_notes'


class TUsers(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    latitude = models.FloatField()
    longitude = models.FloatField()
    lasttime = models.DateTimeField()
    status = models.CharField(max_length=125)
    visible = models.IntegerField()
    about = models.CharField(max_length=255)
    photo50 = models.CharField(max_length=255)
    photo100 = models.CharField(max_length=255)
    photo200 = models.CharField(max_length=255)
    reg_ip = models.CharField(max_length=255)
    from_city = models.CharField(max_length=25)
    data_reg = models.DateTimeField()
    birthday = models.DateField()
    vkid = models.IntegerField()
    gender = models.IntegerField()
    lang = models.CharField(max_length=50)
    fbid = models.IntegerField()
    time_trip = models.TimeField()
    skype = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    jobs = models.CharField(max_length=250)
    study = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_users'
