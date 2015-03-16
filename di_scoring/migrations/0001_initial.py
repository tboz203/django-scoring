# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IC_Appraiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IC_Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time', models.DateTimeField()),
            ],
            options={
                'ordering': ['time'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IC_Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('value', models.CharField(max_length=32)),
                ('ic_appraiser', models.ForeignKey(to='di_scoring.IC_Appraiser')),
                ('ic_event', models.ForeignKey(to='di_scoring.IC_Event')),
            ],
            options={
                'ordering': ['ic_event'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('phone_number', models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message='Phone number must be entered in the format: +999999999 Up to 15 digits allowed.')])),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TC_Appraiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TC_Appraiser_Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tc_appraiser', models.ForeignKey(to='di_scoring.TC_Appraiser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TC_Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('location', models.ForeignKey(to='di_scoring.Location')),
            ],
            options={
                'ordering': ['time'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TC_Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('field_type', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TC_Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('value', models.CharField(max_length=32)),
                ('tc_appraiser', models.ForeignKey(to='di_scoring.TC_Appraiser')),
                ('tc_event', models.ForeignKey(to='di_scoring.TC_Event')),
                ('tc_field', models.ForeignKey(to='di_scoring.TC_Field')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('classification', models.CharField(max_length=1, choices=[('E', 'Elementary'), ('M', 'Middle'), ('H', 'High'), ('U', 'University')])),
                ('manager', models.ForeignKey(to='di_scoring.Manager')),
                ('school', models.ForeignKey(to='di_scoring.School')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamChallenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tc_field',
            name='team_challenge',
            field=models.ForeignKey(to='di_scoring.TeamChallenge'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tc_event',
            name='team',
            field=models.ForeignKey(unique=True, to='di_scoring.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tc_event',
            name='team_challenge',
            field=models.ForeignKey(to='di_scoring.TeamChallenge'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tc_appraiser_permission',
            name='tc_field',
            field=models.ForeignKey(to='di_scoring.TC_Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tc_appraiser',
            name='team_challenge',
            field=models.ForeignKey(to='di_scoring.TeamChallenge'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ic_event',
            name='location',
            field=models.ForeignKey(unique=True, to='di_scoring.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ic_event',
            name='team',
            field=models.ForeignKey(unique=True, to='di_scoring.Team'),
            preserve_default=True,
        ),
    ]
