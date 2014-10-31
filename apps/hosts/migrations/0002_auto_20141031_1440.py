# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='var',
            name='value',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
