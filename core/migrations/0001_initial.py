# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('death_breath_count', models.IntegerField()),
                ('legendary_count', models.IntegerField()),
                ('bounty_count', models.IntegerField()),
                ('blood_shard_count', models.IntegerField()),
                ('experience_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FarmGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='farmevent',
            name='group',
            field=models.ForeignKey(to='core.FarmGroup'),
        ),
    ]
