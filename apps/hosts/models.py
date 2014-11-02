# -*- coding:utf-8 -*-
from django.db import models

from apps.conf.models import VarDef, VarGroupDef


class Host(models.Model):
    '''Hosts.
    '''

    name = models.CharField(
        max_length=200,
        blank=True,
    )
    var_group = models.ManyToManyField(
        VarGroupDef,
        through='HostVarGroups',
        verbose_name=u'Grup de variables',
    )

    def __unicode__(self):
        return u"%s" % self.name


class HostGroup(models.Model):
    ''' Grups de hosts
    '''

    name = models.CharField(max_length=200)
    hosts = models.ManyToManyField(Host)

    def __unicode__(self):
        return u"%s" % self.name


class Var(models.Model):
    '''Vars amb valor.
    '''

    host = models.ForeignKey(
        Host,
        verbose_name=u'host',
        blank=True,
        null=True,
    )
    host_group = models.ForeignKey(
        HostGroup,
        verbose_name=u'host',
        blank=True,
        null=True,
    )
    host_var_group = models.ForeignKey(
        'hosts.HostVarGroups',
        verbose_name=u'Grup de variables del host',
    )
    var_def = models.ForeignKey(
        VarDef,
        verbose_name=u'definició variable',
    )
    value = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=u'valor',
    )

    def __unicode__(self):
        return u"%s / %s" % (self.host_var_group, self.var_def)


class HostVarGroups(models.Model):
    '''Classe intermèdia per poder afegir múltiples vegades la mateixa
    instància.
    '''

    host = models.ForeignKey(
        Host,
        verbose_name=u'host',
        blank=True,
        null=True,
    )
    host_group = models.ForeignKey(
        HostGroup,
        verbose_name=u'host group',
        blank=True,
        null=True,
    )
    var_group = models.ForeignKey(
        VarGroupDef,
        verbose_name=u'grup de variables',
    )

    def __unicode__(self):
        return u"%s #%s" % (self.var_group, self.pk)

    def save(self, *args, **kwargs):
        '''Cada vegada que es desa una instància de HostVarGroups, es comprova
        que existeixin totes les variables que en depenen, sinó les crea.

        '''

        super(HostVarGroups, self).save(*args, **kwargs)
        self.check_vars()

    def check_vars(self):
        '''Mètode que comprova que existeixin totes les variables que
        depenen d'una instància de HostVarGroups, sinó les crea.

        '''

        try:
            for var in self.var_group.vardef_set.all():
                try:
                    Var.objects.get(
                        host_var_group=self,
                        var_def=var
                    )
                except:
                    Var.objects.create(
                        host=self.host,
                        host_group=self.host_group,
                        host_var_group=self,
                        var_def=var
                    )
        except Exception, e:
            raise e
