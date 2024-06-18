import rsa
import configparser

def decrypt_keys(pri_key,config_file):
    with open(pri_key,'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    encrypted_file = open(config_file,'rb').read()
    decrypted_data = rsa.decrypt(encrypted_file, private_key)

    # Convert decrypted data to string and split it into lines
    config_data = decrypted_data.decode()

    # Parse the config data
    config = configparser.RawConfigParser()
    config.read_string(config_data)
    return dict(config.items('creds'))


    
