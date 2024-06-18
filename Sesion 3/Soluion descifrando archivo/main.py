from decryp import decrypt_key

config=decrypt_key('./passwords/rsa/private_key.pem','./passwords/rsa/config.enc')
print(config)
conn_string = f"host={config['hostname']} dbname={config['database']} user={config['user']} password={config['password']}"
print(conn_string)