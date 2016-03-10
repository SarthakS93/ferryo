# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160310_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_artist',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_organizer',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='lat_position',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='long_position',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='preferences_currency',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='preferences_unit',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='social_facebook',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='social_google',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='social_twitter',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='social_website',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='status',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='zipcode',
        ),
    ]