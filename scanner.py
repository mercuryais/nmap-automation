import subprocess
from logger import logger
from data import data


def scannerf(ip, port, flag):
    script = f"nmap {ip}"
    if port:
        port = f"-p {port}"
        script = script + ' ' + port
    if flag:
        flag = f"-{flag}"
        script = script + ' ' + flag
    result = subprocess.run(script, capture_output=True, text=True)
    print(result.stdout if result.returncode == 0 else result.stderr)
    if result.returncode == 0:
        logger(script)
        data(script)