# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0010_remove_hostvargroups_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('hosts', models.ManyToManyField(to='hosts.Host')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='group',
            name='hosts',
        ),
        migrations.RemoveField(
            model_name='group',
            name='var_group',
        ),
        migrations.RemoveField(
            model_name='groupvar',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupvar',
            name='group_var_group',
        ),
        migrations.RemoveField(
            model_name='groupvar',
            name='var_def',
        ),
        migrations.DeleteModel(
            name='GroupVar',
        ),
        migrations.RemoveField(
            model_name='groupvargroups',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.RemoveField(
            model_name='groupvargroups',
            name='var_group',
        ),
        migrations.DeleteModel(
            name='GroupVarGroups',
        ),
    ]
