# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VarDef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'verbose_name': 'Var Definition',
                'verbose_name_plural': 'Var Definitions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VarGroupDef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'verbose_name': 'Var Group Definition',
                'verbose_name_plural': 'Var Group Definitions',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vardef',
            name='var_group',
            field=models.ForeignKey(to='conf.VarGroupDef'),
            preserve_default=True,
        ),
    ]
