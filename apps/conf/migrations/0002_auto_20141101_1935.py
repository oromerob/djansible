# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VarType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('validator', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vardef',
            name='var_type',
            field=models.ForeignKey(blank=True, to='conf.VarType', null=True),
            preserve_default=True,
        ),
    ]
