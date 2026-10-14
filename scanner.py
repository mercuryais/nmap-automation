from logger import logger
import subprocess


def scanner(ip, port, flag):
    script = ['nmap', '-oX', 'data.xml', ip]
    if port:
        script.extend(['-p', port])
    if flag:
        script.append(f"-{flag}") 
    result = subprocess.run(script, capture_output=True, text=True)
    if result.returncode == 0:
        logger(script)