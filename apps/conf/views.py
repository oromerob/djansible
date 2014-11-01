from django.http import HttpResponse
import json

from apps.hosts.models import *
from apps.conf.models import *
import ansible.runner
import ansible.inventory
from ansible import utils
from ansible import callbacks


def ansible_cb(count): return count+1

def ansible_run(request):
    utils.VERBOSITY = 5
    hola    
    stats = callbacks.AggregateStats()
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    inventory = ansible.inventory.Inventory(['localhost','127.0.0.1'])
    run = ansible.runner.Runner(
        remote_user = 'root',
        remote_pass = 'ubuntu',
        pattern = 'all',
        module_name='ping',
        inventory = inventory,
        callbacks = runner_cb
    ).run()

    return HttpResponse(json.dumps(run, indent=2), content_type="application/json")

def export_json(request):
    # Generate json for group (hosts ans vars)
    hostgroups = HostGroup.objects.all()
    export_groups = {}
    for hostgroup in hostgroups:
        export_groups[hostgroup.name]={ 'hosts' : [], 'vars' : {} }
        for host in hostgroup.hosts.all():
            export_groups[hostgroup.name]['hosts'].append(host.name)

        groups = HostVarGroups.objects.filter(host_group=hostgroup)
        for group in groups:
            if not group.var_group.name in export_groups[hostgroup.name]['vars']: export_groups[hostgroup.name]['vars'][group.var_group.name]=[]
            values = Var.objects.filter(host_group=hostgroup)
            finalvalue={}
            for value in values:
                finalvalue[value.var_def.name]=value.value
            export_groups[hostgroup.name]['vars'][group.var_group.name].append(finalvalue)

    # Generate json for hostvars
    hosts = Host.objects.all()
    export = {}
    for host in hosts:
        if not host.name in export: export[host.name]={}
        groups = HostVarGroups.objects.filter(host=host)
        for group in groups:
            if not group.var_group.name in export[host.name]: export[host.name][group.var_group.name]=[]
            values = Var.objects.filter(host_var_group=group)
            finalvalue={}
            for value in values:
                finalvalue[value.var_def.name]=value.value
            export[host.name][group.var_group.name].append(finalvalue)
                
    # mix and print json
    export_groups['_meta']={ 'hostvars' : export }
    return HttpResponse(json.dumps(export_groups, indent=2), content_type="application/json")

