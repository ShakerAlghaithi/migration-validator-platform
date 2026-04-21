import re

def parse_vlan(output: str):
    """
    Extract VLAN IDs from CLI output
    """
    vlans = []
    for line in output.splitlines():
        match = re.match(r"^(\\d+)", line.strip())
        if match:
            vlans.append(match.group(1))
    return vlans


def parse_interfaces(output: str):
    """
    Extract interface states
    """
    interfaces = []
    for line in output.splitlines():
        if "up" in line or "down" in line:
            interfaces.append(line.strip())
    return interfaces


def parse_routes(output: str):
    """
    Simplified route extraction
    """
    routes = []
    for line in output.splitlines():
        if line.startswith("O") or line.startswith("B") or line.startswith("C"):
            routes.append(line.strip())
    return routes