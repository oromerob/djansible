# -*- coding:utf-8 -*-
from django.db import models

from apps.conf.models import VarKey, VarGroup


class Host(models.Model):
    '''Hosts.

    '''

    name = models.CharField(
        max_length=200,
        blank=True,
    )
    var_group = models.ManyToManyField(
        VarGroup
    )

    def __unicode__(self):
        return self.name

    #def properties(self):
    #    return self.var_set.all()


class Var(models.Model):
    '''Vars amb valor.

    '''

    host = models.ForeignKey(Host)
    var_key = models.ForeignKey(VarKey)
    value = models.CharField(
        max_length=255,
    )
