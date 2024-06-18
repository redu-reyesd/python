from sub_modulo.get_logger import logger_config

def inicializar_logger():
    logger=logger_config()
    logger.debug("estoy en el main")
    a=1
    b=0
    try:
        resultado = a/b
    except:
        logger.error(f' la division por cero no esta permidida')
    

if __name__ == '__main__':
    logger=inicializar_logger()

    