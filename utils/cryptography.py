from cryptography.fernet import Fernet

def encrypt_data(key, data):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()


def decrypt_data(key, data):
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()