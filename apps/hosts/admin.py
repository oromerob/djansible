from django.contrib import admin

from .models import Host, Var, HostVarGroups, HostGroup


class VarInline(admin.TabularInline):
    model = Var
    extra = 0
    readonly_fields = ('var_def', 'host_var_group', )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class HostVarInline(VarInline):
    exclude = ['host_group', ]


class HostGroupVarInline(VarInline):
    exclude = ['host', ]


class VarGroupsInline(admin.StackedInline):
    model = HostVarGroups
    extra = 0


class HostVarGroupsInline(VarGroupsInline):
    exclude = ['host_group', ]


class HostGroupVarGroupsInline(VarGroupsInline):
    exclude = ['host', ]


class HostAdmin(admin.ModelAdmin):
    inlines = [HostVarGroupsInline, HostVarInline, ]


class HostGroupAdmin(admin.ModelAdmin):
    inlines = [HostGroupVarGroupsInline, HostGroupVarInline, ]


admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup, HostGroupAdmin)
