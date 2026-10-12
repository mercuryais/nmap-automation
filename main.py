from parser import input_taker
from scanner import scannerf

def main():
    result = input_taker()
    ip = result.get("IP")
    port = result.get("PORT")
    flag = result.get("FLAG")
    scannerf(ip, port, flag)

if __name__ == "__main__":
    main()