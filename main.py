from cli_handler import cli_handler
from scanner import scanner
from logger import logger
from analyser import *
def main():
    try:
        user_input = cli_handler()
        script, result = scanner(*user_input)
        user_readable()
        logger(f"{script}, 'Success'")
    except:
        print(result.stderr)
        logger(f"{script}, 'Failed'")
if __name__ == "__main__":
    main()