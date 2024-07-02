import json

# Leer el archivo de configuración
with open('./Sesion 4/archivos/config.json', 'r') as file:
    config = json.load(file)

# Acceder a los valores
connection.send_configset(config["verificacion.server.com"]["verify_host"])
server_alive_interval = config['default']['ServerAliveInterval']
compression = config['default']['Compression']
user = config['bitbucket.org']['User']
host_port = config['topsecret.server.com']['Host Port']

print(f"Server Alive Interval: {server_alive_interval}")
print(f"Compression: {compression}")
print(f"User: {user}")
print(f"Host Port: {host_port}")
