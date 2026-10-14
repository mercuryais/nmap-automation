import xml.etree.ElementTree as ET

def analys():
    tree = ET.parse("data.xml")
    root = tree.getroot()
    for host in root.findall("host"):
        address_element = host.find("address")
        addr = address_element.get("addr")
        status_host = host.find('status')
        status = status_host.get('state')
        print(addr, status)
        ports_element = host.find('ports')
        ports = ports_element.findall('port')

        for port in ports:
            protocol = port.get('protocol')
            portid = port.get('portid')
            states = port.find('state')
            state = states.get('state')
            services = port.find('service')
            service = services.get('name')
            print(protocol, portid, state, service)
        os_element = host.find('os')
        osmatch = os_element.find('osmatch')
        os = osmatch.get('name')
        print(os)