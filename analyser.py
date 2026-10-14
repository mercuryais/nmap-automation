import xml.etree.ElementTree as ET
import sys
def analys():
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

        if host.find('os'):
            os_element = host.find('os')
            osmatch_element = os_element.find('osmatch')
            os = osmatch_element.get('name')
            print(os)