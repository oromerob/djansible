# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostVarGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('host', models.ForeignKey(to='hosts.Host')),
                ('var_group', models.ForeignKey(to='conf.VarGroupDef')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
                ('host_var_group', models.ForeignKey(to='hosts.HostVarGroups')),
                ('var_def', models.ForeignKey(to='conf.VarDef')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='var',
            unique_together=set([('host_var_group', 'var_def')]),
        ),
        migrations.AddField(
            model_name='host',
            name='var_group',
            field=models.ManyToManyField(to='conf.VarGroupDef', through='hosts.HostVarGroups'),
            preserve_default=True,
        ),
    ]
