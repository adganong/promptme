# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-19 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prompts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prompts.Genre'),
        ),
    ]
