from cryptography.fernet import Fernet

# Synartiseis gia kryptografisi / apokryptografisi <3
def encrypt_message(msg: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(msg.encode())

def decrypt_message(token: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(token).decode()
