# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_newslist'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslist',
            name='weblinks',
            field=models.CharField(default=b'SOME STRING', max_length=200),
        ),
    ]
