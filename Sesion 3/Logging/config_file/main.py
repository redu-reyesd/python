import logging
from sub_modules.initialize_logging import logger_config


def main():
    logger=logger_config()
    logger.info("Starting")

if __name__ == "__main__":
    main()