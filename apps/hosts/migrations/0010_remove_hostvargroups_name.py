# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0009_remove_groupvargroups_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostvargroups',
            name='name',
        ),
    ]
