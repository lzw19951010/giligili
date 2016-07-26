# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glgl_app', '0002_auto_20160726_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.ImageField(default='media/default/default.jpg', upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos'),
        ),
    ]
