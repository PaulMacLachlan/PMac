# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-22 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0006_auto_20170222_0742'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseManager',
        ),
    ]