import logging
import time
from logging.config import fileConfig

import os
def logger_config():
    print(os.getcwd())
    fileConfig('./logging/config_file/sub_modules/config/logging.ini')
    logger=logging.getLogger('dev')
    logger.debug('Initializing....')
    return logger

if __name__ == "__main__":
    logger_config()