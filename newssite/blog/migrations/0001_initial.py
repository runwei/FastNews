# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyWordsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=200)),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NewsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(null=True, verbose_name=b'date published', blank=True)),
                ('keywords', models.CharField(max_length=200)),
                ('weblinks', models.CharField(default=b'SOME STRING', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShowNewsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=50)),
                ('monthday', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=200)),
                ('weblinks', models.CharField(default=b'SOME STRING', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Username', models.CharField(default=1, max_length=100)),
                ('TravelWeight', models.FloatField(default=1)),
                ('MusicWeight', models.FloatField(default=1)),
                ('PoliticWeight', models.FloatField(default=1)),
                ('EntertainmentWeight', models.FloatField(default=1)),
                ('TechnologyWeight', models.FloatField(default=1)),
            ],
        ),
    ]
