# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0010_auto_20161228_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='title',
        ),
    ]
