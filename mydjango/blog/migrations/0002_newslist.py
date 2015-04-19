# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('keywords', models.CharField(max_length=200)),
            ],
        ),
    ]
