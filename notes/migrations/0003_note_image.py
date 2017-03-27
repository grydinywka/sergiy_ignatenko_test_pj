# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-27 06:00
from __future__ import unicode_literals

from django.db import migrations, models


# def load_notes_users_from_fixture(apps, schema_editor):
#     from django.core.management import call_command
#     call_command("loaddata", "init_notes.json")


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20170322_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='note_images/', verbose_name='Note-image'),
        ),
        # migrations.RunPython(load_notes_users_from_fixture),
    ]