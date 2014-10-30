from django.contrib import admin

from .models import VarKey, VarGroup


class VarKeyInline(admin.StackedInline):
    model = VarKey


class VarGroupAdmin(admin.ModelAdmin):
    inlines = [VarKeyInline, ]


admin.site.register(VarGroup, VarGroupAdmin)
