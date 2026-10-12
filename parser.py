import argparse
import re
def input_taker():
    parser = argparse.ArgumentParser()
    parser.add_argument("scan", help="Call nmap function")
    parser.add_argument("ip", help="IP to target")
    parser.add_argument("-p", help="PORTS to target")

    parser.add_argument("flag", nargs="?",help="Choose flag", choices = ["sS", "A", "F", "Z"])
    args = parser.parse_args()
    pattern_ip = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    while True:
        if args.scan == "scan" and pattern_ip.match(args.ip):
            dict = {"IP": args.ip, "PORT": args.p, "FLAG": args.flag}
            print(dict)
            return dict
        else:
            print("========= Wrong command or wrong Ip ==========")
            break