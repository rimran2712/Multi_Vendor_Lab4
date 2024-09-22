from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
import os
import ipdb
from rich import print

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Multi_Vendor_Lab4/Inventory/config.yaml")

# Clearing the Screen
os.system('clear')


def get_device_info (task):
    task.run (task=napalm_get, getters=["get_facts",
                                        "get_interfaces",
                                        "get_interfaces_ip"
                                        ])

get_device_info_results = nr.run (task=get_device_info)

print_result (get_device_info_results)