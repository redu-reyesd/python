import rsa

#obteine llaves  publicas y privadas RSA
public_key,private_key = rsa.newkeys(2048)

path_public_key='./passwords/rsa/public_key.pem'
path_private_key='./passwords/rsa/private_key.pem'

#crea un acrhivo urilizanto la var path_public_key y escribe la llave publica
with open(path_public_key,'wb') as f:
    f.write(public_key.save_pkcs1("PEM"))

#crea un acrhivo urilizanto la var path_private_key y escribe la llave privada
with open(path_private_key,'wb') as f:
    f.write(private_key.save_pkcs1("PEM")) 