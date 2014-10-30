from django.contrib import admin

from .models import VarKey, VarGroup
from apps.hosts.admin import HostVarGroupsInline


class VarKeyInline(admin.StackedInline):
    model = VarKey


class VarGroupAdmin(admin.ModelAdmin):
    inlines = [HostVarGroupsInline, VarKeyInline, ]


admin.site.register(VarGroup, VarGroupAdmin)
