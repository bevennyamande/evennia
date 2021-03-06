# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-21 22:30
from __future__ import unicode_literals

from django.db import migrations


def update_tags_with_dbmodel(apps, schema_editor):

    ObjectDB = apps.get_model('objects', 'ObjectDB')
    for obj in ObjectDB.objects.all():
        obj.db_attributes.all().update(db_model="objectdb")
        obj.db_tags.all().update(db_model="objectdb")

    AccountDB = apps.get_model('accounts', 'AccountDB')
    for obj in AccountDB.objects.all():
        obj.db_attributes.all().update(db_model="accountdb")
        obj.db_tags.all().update(db_model="accountdb")

    ScriptDB = apps.get_model('scripts', 'ScriptDB')
    for obj in ScriptDB.objects.all():
        obj.db_attributes.all().update(db_model="scriptdb")
        obj.db_tags.all().update(db_model="scriptdb")

    ChannelDB = apps.get_model('comms', 'ChannelDB')
    for obj in ChannelDB.objects.all():
        obj.db_attributes.all().update(db_model="channeldb")
        obj.db_tags.all().update(db_model="channeldb")

    HelpEntry = apps.get_model('help', 'HelpEntry')
    for obj in HelpEntry.objects.all():
        obj.db_tags.all().update(db_model="helpentry")

    Msg = apps.get_model('comms', 'Msg')
    for obj in Msg.objects.all():
        obj.db_tags.all().update(db_model="msg")


class Migration(migrations.Migration):

    dependencies = [
        ('typeclasses', '0005_auto_20160625_1812'),
    ]

    operations = [
        migrations.RunPython(update_tags_with_dbmodel)
    ]
