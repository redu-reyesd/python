import os
import rsa
import configparser
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


# Define the Key Vault and secret details
VAULT_URL = "https://ocptestkeyvault.vault.azure.net/"
SECRET_NAME = "private2"

# Logging Key Vault URL and Secret Name
print(f"Key Vault URL: {VAULT_URL}")
print(f"Secret Name: {SECRET_NAME}")

# Authenticate to Azure Key Vault
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=VAULT_URL, credential=credential)

try:
    # Retrieve the private key from Key Vault as a secret
    secret = secret_client.get_secret(SECRET_NAME)
    private_key_pem = secret.value

    # Load the private key
    private_key = rsa.PrivateKey.load_pkcs1(private_key_pem.encode())

    def decrypt_keys(private_key, config_file):
        # Read the encrypted file
        with open(config_file, 'rb') as f:
            encrypted_data = f.read()
        
        # Decrypt the data using the private key
        decrypted_data = rsa.decrypt(encrypted_data, private_key)
        
        # Convert decrypted data to string
        config_data = decrypted_data.decode()

        # Parse the config data
        config = configparser.RawConfigParser()
        config.read_string(config_data)
        return dict(config.items('creds'))

    # Decrypt the configuration file
    config_file_path = 'encrypted_config.bin'
    creds = decrypt_keys(private_key, config_file_path)
    print("Decrypted credentials:", creds)

except Exception as e:
    print(f"An error occurred: {e}")
