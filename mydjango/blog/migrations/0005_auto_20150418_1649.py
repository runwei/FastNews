# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_keywordslist_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslist',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'date published'),
        ),
    ]
