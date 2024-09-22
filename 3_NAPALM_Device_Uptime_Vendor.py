from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
import os
import ipdb
from rich import print

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Multi_Vendor_Lab4/Inventory/config.yaml")

# Clearing the Screen
os.system('clear')

"""
This program will just pul information from muli vendors devices as in topology
and store the information into inventory, embend information into key and store in inventory
We will program on startucture data we have stored in dictionar key form. We will
print device name with vendor and uptime of device
"""
""""
IPDB Inspection of get_facts

ipdb> pp nr.inventory.hosts['vEOS1']['dev_info']
{'get_facts': {'fqdn': 'vArista-R1',
               'hostname': 'vArista-R1',
               'interface_list': ['Ethernet1',
                                  'Ethernet2',
                                  'Ethernet3',
                                  'Ethernet4',
                                  'Ethernet5',
                                  'Ethernet6',
                                  'Ethernet7',
                                  'Ethernet8',
                                  'Management1'],
               'model': 'vEOS-lab',
               'os_version': '4.29.2F-30634808.4292F',
               'serial_number': 'C415E974EC3877CEA835A9491B5B6194',
               'uptime': 3906.0305342674255,
               'vendor': 'Arista'}}

"""
def get_device_info (task):
    facts_results = task.run (task=napalm_get, getters=["get_facts"])
    task.host['dev_info'] = facts_results.result
    model = task.host['dev_info']['get_facts']['model']
    uptime = task.host['dev_info']['get_facts']['uptime']
    vendor = task.host['dev_info']['get_facts']['vendor']
    
    if vendor == 'Cisco':
        print (f"[green]{task.host} is Cisco device, model is [bold]*** {model} ***[/bold] and uptime {uptime} minutes[/green]")
    elif vendor == 'Arista':
        print (f"[yellow]{task.host} is Arista device, model is [bold]*** {model} ***[/bold] and uptime {uptime} minutes[/yellow]")
    elif vendor == 'Juniper':
        print (f"[blue]{task.host} is Juniper device, model is [bold]*** {model} ***[/bold] and uptime {uptime} minutes[/blue]")
    else:
        print (f"[red]{task.host} is Unknow vendor, model is [bold]*** {model} ***[/bold] and uptime {uptime} minutes[/red]")

get_device_info_results = nr.run (task=get_device_info)

#print_result (get_device_info_results)

#ipdb.set_trace ()