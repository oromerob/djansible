from django.http import HttpResponse
import json

from apps.hosts import models as host_models
#from apps.conf import models as conf_models


def export_json(request):
    hosts = host_models.Host.objects.all()
    export = {}
    for host in hosts:
        if not host in export:
            export[host.name] = {}
        groups = host_models.HostVarGroups.objects.filter(host=host)
        for group in groups:
            if not group.var_group.name in export[host.name]:
                export[host.name][group.var_group.name] = []
            values = host_models.Var.objects.filter(host_var_group=group)
            finalvalue = {}
            for value in values:
                finalvalue[value.var_def.name] = value.value
            export[host.name][group.var_group.name].append(finalvalue)

    return HttpResponse(
        json.dumps(export, indent=3),
        content_type="application/json"
    )
