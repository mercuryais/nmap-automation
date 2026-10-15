import subprocess
from logger import logger_function
def scanner(ip, port, flag):
    script = ['nmap', '-oX', 'data.xml', ip]
    if port:
        script.extend(['-p', port])
    if flag:
        script.append(f"-{flag}") 
    logger_function("Starting to scan")
    subprocess.run(script)
    return script