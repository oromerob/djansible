# -*- coding:utf-8 -*-
from django.db import models


class VarGroupDef(models.Model):
    '''Grups de variables.

    '''

    name = models.CharField(
        max_length=200,
        blank=True,
    )

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = u"Var Group Definition"
        verbose_name_plural = u"Var Group Definitions"


class VarDef(models.Model):
    '''Definició de les variables disponibles.

    '''

    var_group = models.ForeignKey(VarGroupDef)
    name = models.CharField(
        max_length=200,
        blank=True,
    )

    def __unicode__(self):
        return u"%s / %s" % (self.var_group, self.name)

    class Meta:
        verbose_name = u"Var Definition"
        verbose_name_plural = u"Var Definitions"
