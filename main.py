from cli_handler import *
from scanner import *
from logger import *
from analyser import *
def main():

    try:
        user_input = cli_handler()
        script = scanner(*user_input)
        user_readable()
        logger_function(f"{script}, 'Success'")
    except Exception as e:
        print(e)
        logger_function(f"{script}, 'Failed'")
if __name__ == "__main__":
    main()