# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_auto_20141030_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='var',
            name='host',
            field=models.ForeignKey(to='hosts.Host'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='var',
            unique_together=set([('host', 'var_key')]),
        ),
    ]
