# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 23:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glgl_app', '0011_userextraprofile_headimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextraprofile',
            name='headimage',
        ),
    ]