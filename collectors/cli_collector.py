from netmiko import ConnectHandler
from normalization.parser import parse_vlan, parse_interfaces, parse_routes


def collect_device_state(device):
    conn = ConnectHandler(**device)

    vlan_output = conn.send_command("show vlan brief")
    int_output = conn.send_command("show ip interface brief")
    route_output = conn.send_command("show ip route")

    state = {
        "vlans": parse_vlan(vlan_output),
        "interfaces": parse_interfaces(int_output),
        "routes": parse_routes(route_output),
    }

    conn.disconnect()
    return state