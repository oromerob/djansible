from django.contrib import admin

from .models import Host, Var, HostVarGroups, Group, GroupVar, GroupVarGroups


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

class GroupVarGroupsInline(admin.StackedInline):
	model = GroupVarGroups
	extra = 0

class GroupVarInline(admin.TabularInline):
	model = GroupVar
	extra = 0
	readonly_fields = ('var_def', 'group_var_group', )
	readonly_fields = ('var_def',  )
	
	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

class GroupAdmin(admin.ModelAdmin):
	inlines = [GroupVarGroupsInline, GroupVarInline, ]

admin.site.register(Host, HostAdmin)
admin.site.register(Group, GroupAdmin)
