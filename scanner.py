from logger import logger
from data import *


def scanner(ip, port, flag):
    script = f"nmap {ip}"
    if port:
        script = f"{script} -p {port}"
    if flag:
        script = f"{script} -{flag}"
    result = subprocess.run(script, capture_output=True, text=True)
    print(result.stdout if result.returncode == 0 else result.stderr)
    if result.returncode == 0:
        logger(script)
        data(script)