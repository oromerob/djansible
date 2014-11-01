# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0011_auto_20141031_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostvargroups',
            name='host_group',
            field=models.ForeignKey(verbose_name='host group', blank=True, to='hosts.HostGroup', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hostvargroups',
            name='host',
            field=models.ForeignKey(verbose_name='host', blank=True, to='hosts.Host', null=True),
            preserve_default=True,
        ),
    ]
