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

               
IPDB Inspection of "get_interfaces"
ipdb> pp nr.inventory.hosts['vIOS1']['interfaces_info']

{'get_interfaces': {'GigabitEthernet0/0': {'description': '',
                                           'is_enabled': True,
                                           'is_up': True,
                                           'last_flapped': -1.0,
                                           'mac_address': '50:60:F6:00:13:00',
                                           'mtu': 1500,
                                           'speed': 1000.0},
                    'GigabitEthernet0/1': {'description': '',
                                           'is_enabled': False,
                                           'is_up': False,
                                           'last_flapped': -1.0,
                                           'mac_address': '50:60:F6:00:13:01',
                                           'mtu': 1500,
                                           'speed': 1000.0},
                    'GigabitEthernet0/2': {'description': '',
                                           'is_enabled': False,
                                           'is_up': False,
                                           'last_flapped': -1.0,
                                           'mac_address': '50:60:F6:00:13:02',
                                           'mtu': 1500,
                                           'speed': 1000.0},
                    'GigabitEthernet0/3': {'description': '',
                                           'is_enabled': False,
                                           'is_up': False,
                                           'last_flapped': -1.0,
                                           'mac_address': '50:60:F6:00:13:03',
                                           'mtu': 1500,
                                           'speed': 1000.0}}}





IPDB Inspection of "get_interfaces_ip"

ipdb> pp nr.inventory.hosts['vQFX-RE1']['interfaces_ip_info']
{'get_interfaces_ip': {'bme0.0': {'ipv4': {'128.0.0.1': {'prefix_length': 2},
                                           '128.0.0.16': {'prefix_length': 2},
                                           '128.0.0.4': {'prefix_length': 2},
                                           '128.0.0.63': {'prefix_length': 2}}},
                       'em0.0': {'ipv4': {'172.16.100.10': {'prefix_length': 30}}},
                       'em1.0': {'ipv4': {'169.254.0.2': {'prefix_length': 24}}},
                       'em2.32768': {'ipv4': {'192.168.1.2': {'prefix_length': 24}}},
                       'em4.32768': {'ipv4': {'192.0.2.2': {'prefix_length': 24}}},
                       'jsrv.1': {'ipv4': {'128.0.0.127': {'prefix_length': 2}}},
                       'lo0.0': {'ipv6': {'fe80::205:860f:fc71:d300': {'prefix_length': 128}}}}}

"""
def get_device_info (task):
    facts_results = task.run (task=napalm_get, getters=["get_facts"])
    interfaces_results = task.run (task=napalm_get, getters=["get_interfaces"])
    interfaces_ip_results = task.run (task=napalm_get, getters=["get_interfaces_ip"])
    
    task.host['dev_info'] = facts_results.result
    task.host['interfaces_info'] = interfaces_results.result
    task.host['interfaces_ip_info'] = interfaces_ip_results.result

get_device_info_results = nr.run (task=get_device_info)

#print_result (get_device_info_results)

ipdb.set_trace ()