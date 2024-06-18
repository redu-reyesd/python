import logging
import time
from logging.config import fileConfig
import os

def logger_config():
    fileConfig('./logueo/sub_modulo/config.ini')
    logger=logging.getLogger('root')
    logger.debug('inicializando')
    logger.warning('inicializando')
    return logger


logger=logger_config()



