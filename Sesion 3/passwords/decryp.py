import rsa
import configparser

def decrypt_key(private_key,config_file):
    #abre la llave privada y l asigna a la variable private_key
    with open(private_key,'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    #abre el archivo encriptado en forma de lectura
    encrypted_file = open(config_file,'rb').read()
    
    #decripta el archivo usando la llave privada y l asigna a la variable decrypeted
    decrypted = rsa.decrypt(encrypted_file,private_key)    
    
    #configura el resultado en fomato string
    config_data = decrypted.decode()
    
    #inicializa un config paras
    config = configparser.RawConfigParser()
    
    #leee el string de la varible y lo convierte en un formato de configuracion
    config.read_string(config_data)
    print(config)
    #retorna un diccionario
    return dict(config.items('creds'))
