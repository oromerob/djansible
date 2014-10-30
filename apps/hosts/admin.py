from django.contrib import admin
from django import forms

from .models import Host, Var
from apps.conf.models import VarKey


class VarInline(admin.StackedInline):
    model = Var

    def formfield_for_dbfield(self, field, **kwargs):
        if field.name == 'var_key':
            parent_host = self.get_object(kwargs['request'], Host)
            var_keys = []
            groups = parent_host.var_group.all().distinct()
            properties = VarKey.objects.filter(var_group__in=groups)
            return forms.ModelChoiceField(queryset=properties)
        return super(VarInline, self).formfield_for_dbfield(field, **kwargs)

    def get_object(self, request, model):
        object_id = request.META['PATH_INFO'].strip('/').split('/')[-1]
        try:
            object_id = int(object_id)
        except ValueError:
            return None
        return model.objects.get(pk=object_id)


class HostAdmin(admin.ModelAdmin):
    inlines = [VarInline, ]


admin.site.register(Host, HostAdmin)
