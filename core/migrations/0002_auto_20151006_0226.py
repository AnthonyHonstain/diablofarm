# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmevent',
            name='blood_shard_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='farmevent',
            name='bounty_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='farmevent',
            name='death_breath_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='farmevent',
            name='experience_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='farmevent',
            name='legendary_count',
            field=models.IntegerField(null=True),
        ),
    ]
