from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks/Multi_Vendor_Lab4/Inventory/config.yaml")

def get_device_info (task):
    task.run (task=napalm_get, getters=["get_facts",
                                        "get_interfaces",
                                        "get_interfaces_ip"
                                        ])

get_device_info_results = nr.run (task=get_device_info)

print_result (get_device_info_results)