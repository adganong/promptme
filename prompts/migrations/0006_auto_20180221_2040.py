# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prompts', '0005_auto_20180219_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='builtprompt',
            name='prompt_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='builtprompt',
            name='prompt_person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prompt_person', to='prompts.PromptPiece'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='builtprompt',
            name='prompt_place',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prompt_place', to='prompts.PromptPiece'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='builtprompt',
            name='prompt_scenario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prompt_scenario', to='prompts.PromptPiece'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='builtprompt',
            name='prompt_thing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prompt_thing', to='prompts.PromptPiece'),
            preserve_default=False,
        ),
    ]
