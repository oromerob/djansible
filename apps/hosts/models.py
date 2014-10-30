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
        VarGroup,
        through='HostVarGroups',
    )

    def __unicode__(self):
        return u"%s" % self.name

    def properties(self):
        return self.var_set.all()


class Var(models.Model):
    '''Vars amb valor.

    '''

    host = models.ForeignKey(Host)
    var_key = models.ForeignKey(VarKey)
    value = models.CharField(
        max_length=255,
    )

    def __unicode__(self):
        return u"%s / %s" % (self.host, self.var_key)

    class Meta:
        unique_together = (("host", "var_key"),)


class HostVarGroups(models.Model):
    '''Taula intermitja per poder afegir múltiples vegades la mateixa
    instància.

    '''

    host = models.ForeignKey(Host)
    var_group = models.ForeignKey(VarGroup)
