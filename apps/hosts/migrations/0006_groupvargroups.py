# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
        ('hosts', '0005_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupVarGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='nom', blank=True)),
                ('group', models.ForeignKey(verbose_name='host', to='hosts.Group')),
                ('var_group', models.ForeignKey(verbose_name='grup de variables', to='conf.VarGroupDef')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
