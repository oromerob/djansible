from django.contrib import admin
#from django import forms

from .models import Host, Var


class VarInline(admin.TabularInline):
    model = Var


class HostAdmin(admin.ModelAdmin):
    inlines = [VarInline, ]


admin.site.register(Host, HostAdmin)
