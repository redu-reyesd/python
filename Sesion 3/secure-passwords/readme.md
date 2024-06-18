## Hashing VS Encripcion:
- Hashing: es una técnica unidireccional en donde se convierte una contraseña en una cadena con un tamaño definido de caracteres. Dado que es un proceso unidireccional, no es un proceso reversible, a diferencia de la encriptación.
    - MD5
    - SHA-1
    - SHA-256, SHA-384, SHA-512: todos ellos forman parte de SHA-2
    - SHA-3
- Encriptación: Es un proceso bidireccional en donde se cifran los datos utilizando una llave secreta para convertir la información a una forma encriptada. Dado que el proceso requiere de una llave secreta, es un proceso reversible, es decir si alguien llegase a obtener acceso a esa llave podría revertir el proceso y obtener acceso a la data. 


## Encrypting config data using openssl:

El cifrado de los datos de require de 2 factores:
- Una llave rsa privada para descifrar el mensaje
- Una llave publica para cifrar el mensaje

Haga uso del siguiente codigo para generar una llave privada y una llave publica:

```python

import rsa
public_key,private_key = rsa.newkeys(2048)
public='./secure-passwords/rsa_keys/public-key.pem'
private='./secure-passwords/rsa_keys/private-key.pem'

with open(public,'wb') as f:
    f.write(public_key.save_pkcs1("PEM"))

with open(private,'wb') as f:
    f.write(private_key.save_pkcs1("PEM")) 
    
if __name__ == "__main__":
    main()

```

Con las pasos anteriores tenemos todos los insumos necesario para poder iniciar con el cifrado de los datos.

Tomemos como ejemplo el siguiente archivo de configuracion :
```python
[creds]
Hostname    = hh-pgsql-public.ebi.ac.uk
Port        = 5432
Database    = pfmegrnargs
User        = reader
Password    = NWDMCE5xdipIjRrp
```

Utilice la llave publica generada en el paso anterior para cifrar el archivo.


```bash
 openssl rsautl -encrypt -inkey ./public-key.pem -pubin -in ./someconfigfile.cfg -out someconfigfile.enc
```

## Descifrando el archivo con OpenSSL

Para descifrar el archivo ejecute haga uso de la llave privada, de la siguiente manera
```bash
openssl rsautl -decrypt -inkey ./private-key.pem -in ./someconfigfile.enc -out someconfigfile.decrypted
```

## Descifrando el archivo con Python

```python
import rsa
import configparser

def decrypt_keys(pri_key,config_file):
    with open(pri_key,'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    encrypted_file = open(config_file,'rb').read()
    decrypted_data = rsa.decrypt(encrypted_file, private_key)

    #convert the encrypted to plaintext 
    config_data = decrypted_data.decode()

    # Parse the config data
    config = configparser.RawConfigParser()
    config.read_string(config_data)
    #return a dictionaty with the config data
    return dict(config.items('creds'))
```


# REFERENCIAS

Aryan Irani. (2021, March 9). Working with Files in Python. Welcome ! | by Aryan Irani | Medium. https://aryanirani123.medium.com/working-with-files-in-python-31e17f4861b

  James H.Ellis, Clifford Cocks, Ron Rivest, Leonard M. Adleman, & Adi Shamir. (n.d.). Encrypt/Decrypt a file using RSA public-private key pair | what-why-how. Retrieved June 5, 2024, from https://kulkarniamit.github.io/whatwhyhow/howto/encrypt-decrypt-file-using-rsa-public-private-keys.html

  M&E Technical Solutions Ltd. (2023, March 27). Python by Examples: RSA encryption & decryption | by M&E Technical Solutions Ltd. | Medium. https://medium.com/@metechsolutions/python-by-examples-rsa-encryption-decryption-d07a226430b4

  NeuralNine. (n.d.). (15) RSA Private & Public Key Encryption in Python - YouTube. Retrieved June 5, 2024, from https://www.youtube.com/watch?v=n0uJsqFGO4k&ab_channel=NeuralNine

  Scott Brady. (2020, August 5). Creating RSA Keys using OpenSSL. https://www.scottbrady91.com/openssl/creating-rsa-keys-using-openssl

  Sima Zhu, Scott Beddall, & McCoy Patiño. (2024, February 28). Azure Key Vault Keys client library for Python | Microsoft Learn. https://learn.microsoft.com/en-us/python/api/overview/azure/keyvault-keys-readme?view=azure-python

  stuvel.eu. (n.d.). 8. Reference — Python-RSA 4.8 documentation. Retrieved June 5, 2024, from https://stuvel.eu/python-rsa-doc/reference.html
  