
import logging

# Add handlers to the logger



logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
def init_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) 
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('app.log')

    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - __%(funcName)s__  - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

def test(logger):
    logger.info('Testing')
    
def main():
    logger = init_logger()
   
    logger.info('This is an info message')
    test(logger)
    logger.info('Hola')
    logging.warning('Atento.!!')  
    logging.info('Te lo dije.!!')  
    logging.warning('Atento.!!')  
    logging.info('Te lo dije.!!')
    
if __name__ == "__main__":
    main()