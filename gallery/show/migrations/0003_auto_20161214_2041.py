# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_gallery_keyword'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gallery',
            new_name='Image',
        ),
    ]