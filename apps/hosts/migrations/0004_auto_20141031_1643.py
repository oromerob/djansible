# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0003_var_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='var_group',
            field=models.ManyToManyField(to='conf.VarGroupDef', verbose_name='Grup de variables', through='hosts.HostVarGroups'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hostvargroups',
            name='host',
            field=models.ForeignKey(verbose_name='host', to='hosts.Host'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hostvargroups',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nom', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hostvargroups',
            name='var_group',
            field=models.ForeignKey(verbose_name='grup de variables', to='conf.VarGroupDef'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='var',
            name='host',
            field=models.ForeignKey(verbose_name='host', to='hosts.Host'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='var',
            name='host_var_group',
            field=models.ForeignKey(verbose_name='Grup de variables del host', to='hosts.HostVarGroups'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='var',
            name='value',
            field=models.CharField(max_length=255, verbose_name='valor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='var',
            name='var_def',
            field=models.ForeignKey(verbose_name='definici\xf3 variable', to='conf.VarDef'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='var',
            unique_together=set([]),
        ),
    ]
