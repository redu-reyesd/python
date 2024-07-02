import logging
from logging.config import fileConfig
import configparser

def log_parser(file_config):
    fileConfig(file_config)
    logger= logging.getLogger("root")
    logger.debug('inicializando')
    logger.warning('inicializando')
    return logger

def  get_config_files(file_name,section=None):
    ''' 
    :params :
        file_name = config file with files for logging config, creds, etc.
        section = section to import it will allow null values
    '''
    config = configparser.ConfigParser()
    config.read(file_name)
    if not section:
        return config
    
    return dict(config[section])
    

if __name__ == "__main__":
    log_parser('./configs/logging.ini')