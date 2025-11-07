from cryptography.fernet import Fernet

def generate_key():
    # Generate a new key and returns it
    return Fernet.generate_key().decode()