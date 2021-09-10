import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

host_ip = os.environ['HOST_IP']
vips = [os.environ['IP']]
vrrpid = os.environ.get('ID')
mac = os.environ.get('MAC')
url = "https://%s:8082" % host_ip
data = requests.get("%s/virtual-machine-interfaces" % url, verify=False).json()['virtual-machine-interfaces']

for entry in data:
    if 'vhost0' in entry['fq_name']:
        host = entry['fq_name'][1]
        href = entry['href']
        nodedata = requests.get(href, verify=False).json()['virtual-machine-interface']
        found_vips = []
        allowed_address_pairs = []
        if 'virtual_machine_interface_allowed_address_pairs' in nodedata:
            allowed_address_pairs = nodedata['virtual_machine_interface_allowed_address_pairs']['allowed_address_pair']
            for ip in allowed_address_pairs:
                for vip in vips:
                    if ip['ip']['ip_prefix'] == vip:
                        found_vips.append(vip)
        missing_vips = [ip for ip in vips if ip not in found_vips]
        for vip in missing_vips:
            print("Adding vip %s in %s" % (vip, host))
            newentry = {'ip': {'ip_prefix': vip, 'ip_prefix_len': 32}, 'address_mode': 'active-standby'}
            if vrrpid is not None:
                 virtual_router_id_hex = format(int(vrrpid), 'x')
                 if len(virtual_router_id_hex) == 1:
                     virtual_router_id_hex = "0%s" % virtual_router_id_hex
                 mac = "00:00:5e:00:01:%s" % virtual_router_id_hex
            if mac is not None:
                newentry['mac'] = mac
            allowed_address_pairs.append(newentry)
            new = {'virtual_machine_interface_allowed_address_pairs': {'allowed_address_pair': allowed_address_pairs}}
            body = {'virtual-machine-interface': new}
            requests.put(href, verify=False, json=body)
