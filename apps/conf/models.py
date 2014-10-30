# -*- coding:utf-8 -*-
from django.db import models


class VarGroup(models.Model):
    '''Grups de variables.

    '''

    name = models.CharField(
        max_length=200,
        blank=True,
    )

    def __unicode__(self):
        return self.name


class VarKey(models.Model):
    '''Definició de les variables disponibles.

    '''

    var_group = models.ForeignKey(VarGroup)
    name = models.CharField(
        max_length=200,
        blank=True,
    )

    def __unicode__(self):
        return "%s / %s" % (self.var_group, self.name)
