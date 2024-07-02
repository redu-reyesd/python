import yaml

# Leer el archivo de configuración
with open('./Sesion 4/archivos/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Acceder a los valores
server_alive_interval = config['default']['ServerAliveInterval']
compression = config['default']['Compression']
user = config['bitbucket.org']['User']
host_port = config['topsecret.server.com']['Host Port']

print(f"Server Alive Interval: {server_alive_interval}")
print(f"Compression: {compression}")
print(f"User: {user}")
print(f"Host Port: {host_port}")
