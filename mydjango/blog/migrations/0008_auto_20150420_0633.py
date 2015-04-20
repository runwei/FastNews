# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150419_0346'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='ContactPost',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
