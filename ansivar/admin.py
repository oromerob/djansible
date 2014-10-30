from django.contrib import admin
from ansivar.models import Host, VarGroup, VarKey, VarName, VarValue


class VarValueInline(admin.StackedInline):
	model = VarValue

class VarKeyAdmin(admin.ModelAdmin):
	list_display = [ 'id', 'host', 'var_group' ]
	inlines = [ VarValueInline ]


class VarValueAdmin(admin.ModelAdmin):
	fields = [ 'var_key', 'var_name', 'value' ]

admin.site.register(Host)
admin.site.register(VarGroup)
admin.site.register(VarKey, VarKeyAdmin)
admin.site.register(VarName)
admin.site.register(VarValue)
