import logging
def logger(script):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("logs.log", mode="a")
    formatter = logging.Formatter("%(asctime)s \n%(message)s ")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug(script)

if __name__ == "__main__":
    logger()