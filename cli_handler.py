import argparse
def cli_handler():
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="Ip to target")
    parser.add_argument("-p", help="Ports to target")
    parser.add_argument("flag", nargs="?",help="Choose flag", choices = ["sS", "A", "F", "O"])
    args = parser.parse_args()
    return (args.ip, args.p, args.flag)