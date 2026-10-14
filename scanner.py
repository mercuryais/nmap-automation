import subprocess
from logger import logger 
def scanner(ip, port, flag):
    script = ['nmap', '-oX', 'data.xml', ip]
    if port:
        script.extend(['-p', port])
    if flag:
        script.append(f"-{flag}") 
    logger("Starting to scan")
    return (script, subprocess.run(script, capture_output=True, text=True))