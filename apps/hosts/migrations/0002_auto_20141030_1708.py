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
            name='host',
            field=models.OneToOneField(to='hosts.Host'),
            preserve_default=True,
        ),
    ]
