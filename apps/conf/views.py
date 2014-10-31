from django.http import HttpResponse
from django.template import RequestContext, loader

from apps.hosts.models import *
from apps.conf.models import *

import json


def export_json(request):
	hosts = Host.objects.all()
	export = {}
	for host in hosts:
		if not host in export: export[host.name]={}
		groups = HostVarGroups.objects.filter(host=host)
		for group in groups:
			if not group in export[host.name]: export[host.name][group.var_group.name]=[]
			values = Var.objects.filter(host_var_group=group)
			finalvalue={}
			for value in values:
				finalvalue[value.var_def.name]=value.value
			export[host.name][group.var_group.name].append(finalvalue)
				
	return HttpResponse(json.dumps(export, indent=3), content_type="application/json")

