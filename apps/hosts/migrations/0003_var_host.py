# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_auto_20141031_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='var',
            name='host',
            field=models.ForeignKey(default=1, to='hosts.Host'),
            preserve_default=False,
        ),
    ]
