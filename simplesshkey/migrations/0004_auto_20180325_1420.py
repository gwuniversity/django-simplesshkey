# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-25 14:20
from __future__ import unicode_literals

from django.db import migrations

from simplesshkey.util import PublicKeyParseError, pubkey_parse

def populate_keytype(apps, schema_editor):
    SSHKey = apps.get_model('simplesshkey', 'userkey')
    for key in SSHKey.objects.all():
        if not key.key:
            continue
        try:
            pubkey = pubkey_parse(key.key)
        except PublicKeyParseError as e:
            continue
        key.keytype = pubkey.keytype()
        key.save()

class Migration(migrations.Migration):

    dependencies = [
        ('simplesshkey', '0003_userkey_keytype'),
    ]

    operations = [
        migrations.RunPython(populate_keytype, migrations.RunPython.noop),
    ]
