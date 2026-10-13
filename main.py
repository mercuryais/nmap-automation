from cli_handler import cli_handler
from scanner import scanner
def main():
    result = cli_handler()
    scanner(*result)
if __name__ == "__main__":
    main()