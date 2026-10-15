import logging

logger_var = logging.getLogger(__name__)
logger_var.setLevel(logging.DEBUG)
handler = logging.FileHandler("logs.log", mode="a")
formatter = logging.Formatter("%(asctime)s %(message)s ")
handler.setFormatter(formatter)
logger_var.addHandler(handler)

def logger_function(messages):
    logger_var.info(messages)

if __name__ == "__main__":
    logger_function()