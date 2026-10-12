import subprocess
def scannerf(ip, port, flag):
    script = f"nmap {ip}"
    if port:
        port = f"-p {port}"
        if flag:
            flag = f"-{flag}"
            subprocess.run(f"{script} {port} {flag}")
        else:
            subprocess.run(f"{script} {port}")
    else:
        subprocess.run(script)