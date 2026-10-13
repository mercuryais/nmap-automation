from parser import input_taker
from scanner import scannerf
import sys
def main():
    try:
        result = input_taker()
        ip = result.get("IP")
        port = result.get("PORT")
        flag = result.get("FLAG")
        scannerf(ip, port, flag)
    except:
        print("Error occured.")
        sys.exit(1)
if __name__ == "__main__":
    main()