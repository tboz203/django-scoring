# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('di_scoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ic_appraiser',
            options={'verbose_name': 'Instant Challenge Appraiser', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='ic_event',
            options={'verbose_name': 'Instant Challenge Event', 'ordering': ['time']},
        ),
        migrations.AlterModelOptions(
            name='ic_score',
            options={'verbose_name': 'Instant Challenge Score', 'ordering': ['ic_event']},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Team Manager', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tc_appraiser',
            options={'verbose_name': 'Team Challenge Appraiser', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tc_appraiser_permission',
            options={'verbose_name': 'Team Challenge Appraiser Permission', 'ordering': ['tc_appraiser']},
        ),
        migrations.AlterModelOptions(
            name='tc_event',
            options={'verbose_name': 'Team Challenge Event', 'ordering': ['time']},
        ),
        migrations.AlterModelOptions(
            name='tc_field',
            options={'verbose_name': 'Team Challenge Scoring Field', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tc_score',
            options={'verbose_name': 'Team Challenge Score'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['classification', 'name']},
        ),
        migrations.AlterModelOptions(
            name='teamchallenge',
            options={'verbose_name': 'Team Challenge', 'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='team',
            name='team_challenge',
            field=models.ForeignKey(default=0, to='di_scoring.TeamChallenge'),
            preserve_default=False,
        ),
    ]
