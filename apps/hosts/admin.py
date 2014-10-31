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


class HostVarGroupsInline(admin.StackedInline):
    model = HostVarGroups
    extra = 0


class HostAdmin(admin.ModelAdmin):
    inlines = [HostVarGroupsInline, VarInline, ]


admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup)
