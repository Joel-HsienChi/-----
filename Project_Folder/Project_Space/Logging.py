import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")


x = 2
logging.info(f"the value of x is {x}") 

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("test", exc_info=True)

logger = logging.getLogger(__name__)

handler = logging.FileHandler('test.log')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("test the custom logger")