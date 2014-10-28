from django.contrib import admin
from ansivar.models import Host, VarGroup, VarKey, VarName, VarValue

admin.site.register(Host)
admin.site.register(VarGroup)
admin.site.register(VarKey)
admin.site.register(VarName)
admin.site.register(VarValue)
