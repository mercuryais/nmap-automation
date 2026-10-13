import argparse
import re
import sys
def cli_handler():
    parser = argparse.ArgumentParser()
    parser.add_argument("scan", help="Call nmap")
    parser.add_argument("ip", help="Ip to target")
    parser.add_argument("-p", help="Ports to target")
    parser.add_argument("flag", nargs="?",help="Choose flag", choices = ["sS", "A", "F", "Z"])
    args = parser.parse_args()
    pattern_ip = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if args.scan == "scan" and pattern_ip.match(args.ip):
        return (args.ip, args.p, args.flag)
    else:
        print("========= Wrong command or wrong Ip ==========")
        sys.exit(1)