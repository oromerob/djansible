# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
        ('hosts', '0007_groupvar'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='var_group',
            field=models.ManyToManyField(to='conf.VarGroupDef', verbose_name='Grup de variables pel grup', through='hosts.GroupVarGroups'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='groupvargroups',
            name='group',
            field=models.ForeignKey(verbose_name='grup', to='hosts.Group'),
            preserve_default=True,
        ),
    ]
