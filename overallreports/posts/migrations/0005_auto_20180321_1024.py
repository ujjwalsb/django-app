# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=0, unique=True),
        ),
    ]
