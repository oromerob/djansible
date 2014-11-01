from django.contrib import admin

from .models import Host, Var, HostVarGroups, HostGroup
from .forms import VarModelForm


from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class VarInline(NestedStackedInline,):
    model = Var
    form = VarModelForm
    extra = 0
#    readonly_fields = ('var_def', 'host_var_group', )
    fields = [ 'value', ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class HostVarInline(VarInline):
    exclude = ['host_group', ]


class HostGroupVarInline(VarInline):
    exclude = ['host', ]


class VarGroupsInline(NestedStackedInline,):
    model = HostVarGroups
    extra = 0


class HostVarGroupsInline(VarGroupsInline):
    exclude = ['host_group', ]
    inlines = [ HostVarInline, ]


class HostGroupVarGroupsInline(VarGroupsInline):
    exclude = ['host', ]
    inlines = [ HostGroupVarInline, ]


class HostAdmin(NestedModelAdmin):
    inlines = [ HostVarGroupsInline, ]


class HostGroupAdmin(NestedModelAdmin):
    inlines = [HostGroupVarGroupsInline, ]


admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup, HostGroupAdmin)
