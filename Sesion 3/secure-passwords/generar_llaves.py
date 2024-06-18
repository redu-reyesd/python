import rsa
public_key,private_key = rsa.newkeys(2048)


with open('./secure-passwords/rsa_keys/public-key.pem','wb') as f:
    f.write(public_key.save_pkcs1("PEM"))

with open('./secure-passwords/rsa_keys/private-key.pem','wb') as f:
    f.write(private_key.save_pkcs1("PEM")) 