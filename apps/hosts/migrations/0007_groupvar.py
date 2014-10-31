# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
        ('hosts', '0006_groupvargroups'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupVar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255, verbose_name='valor', blank=True)),
                ('group', models.ForeignKey(verbose_name='group', to='hosts.Group')),
                ('group_var_group', models.ForeignKey(verbose_name='Grup de variables del grup', to='hosts.GroupVarGroups')),
                ('var_def', models.ForeignKey(verbose_name='definici\xf3 variable', to='conf.VarDef')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
