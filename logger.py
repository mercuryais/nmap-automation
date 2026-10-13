import logging
def logger(result):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("logs.log", mode="a")
    formatter = logging.Formatter("%(asctime)s \n%(message)s ")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug(result)


if __name__ == "__main__":
    logger()