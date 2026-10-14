import logging


def logger(messages):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("logs.log", mode="a")
    formatter = logging.Formatter("%(asctime)s %(message)s ")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(messages)

if __name__ == "__main__":
    logger()
# wheter succesful or not