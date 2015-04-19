# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_shownewslist_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='keyword',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='weight',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='EntertainmentWeight',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='MusicWeight',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='PoliticWeight',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='TechnologyWeight',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='TravelWeight',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Username',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
