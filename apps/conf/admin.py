from django.contrib import admin

from .models import VarDef, VarGroupDef, VarType


class VarDefInline(admin.StackedInline):
    model = VarDef


class VarGroupDefAdmin(admin.ModelAdmin):
    inlines = [VarDefInline, ]


admin.site.register(VarGroupDef, VarGroupDefAdmin)
admin.site.register(VarType)
