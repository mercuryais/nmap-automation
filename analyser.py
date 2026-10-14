import xml.etree.ElementTree as ET
import sys
def user_readable():
    tree = ET.parse("data.xml")
    root = tree.getroot()
    hosty = root.findall('host')

    if not hosty:
        print("Host not found")
        sys.exit(1)

    for host in hosty:

        address_element = host.find("address")
        addr = address_element.get("addr")

        status_host_element = host.find('status')
        status = status_host_element.get('state')

        print(addr, status)
        open_ports = []
        ports_element = host.find('ports')
        ports = ports_element.findall('port')
        for port in ports:
            protocol = port.get('protocol')
            portid = port.get('portid')
            state_port_element = port.find('state')
            state = state_port_element.get('state')
            services_element = port.find('service')
            service = services_element.get('name')
            print(protocol, portid, state, service)
            if state == "open":
                open_ports.append(portid)

        if host.find('os'):
            os_element = host.find('os')
            osmatch_element = os_element.find('osmatch')
            os = osmatch_element.get('name')
            print(os)
        analyse(open_ports)

def analyse(open_ports):
    risky_ports = {
        '3389': ('OH NOO1', 'CRITICAL'),
        '445': ('OH NOO2', 'CRITICAL'),
        '23': ('OH NOO3', 'CRITICAL'),
        '21': ('OH NOO4', 'HIGH'),
        '22': ('OH NOO5', 'HIGH'),
        '3306': ('OH NOO6', 'HIGH'),
        '6379': ('OH NOO7', 'HIGH'),
        '25': ('OH NOO8', 'Medium'),
        '135': ('OH NOO9', 'Medium'),
        '139': ('OH NOO10', 'Medium'),
        '8443': ('OH NOO11', 'Medium')
    }
    for op in open_ports:
        for rp, info in risky_ports.items():
            if op in rp:
                print(f'Open risky port detected {op} - Risk level {info[1]}')