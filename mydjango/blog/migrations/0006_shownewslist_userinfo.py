# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150418_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowNewsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('keyword', models.CharField(max_length=200)),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
    ]
