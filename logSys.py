import logging
import sys
import time
import os

if not os.path.exists('log/'):
    os.makedirs('log/')

logdatetime = time.strftime("%m-%Y")
logname = "log/" + logdatetime + "_downloader.log"

logging.basicConfig(filename=logname,
                    format='[%(asctime)s] %(levelname)s: %(funcName)s:%(lineno)d %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filemode='a')

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def setAppError(err):
    logger.error(err)

