import configparser

# Crear una instancia de ConfigParser
config = configparser.ConfigParser()

# Leer el archivo de configuración
config.read('./Sesion 4/archivos/config.cfg')

print(config)
# Acceder a los valores
server_alive_interval = config['DEFAULT']['ServerAliveInterval']
compression = config['DEFAULT']['Compression']
user = config['bitbucket.org']['User']
host_port = config['topsecret.server.com']['Host Port']

print(f"Server Alive Interval: {server_alive_interval}")
print(f"Compression: {compression}")
print(f"User: {user}")
print(f"Host Port: {host_port}")
