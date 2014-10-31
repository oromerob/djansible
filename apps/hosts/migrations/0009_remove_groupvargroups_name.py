# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0008_auto_20141031_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupvargroups',
            name='name',
        ),
    ]
