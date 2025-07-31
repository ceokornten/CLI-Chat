from pathlib import Path
from pgpy import PGPKey, PGPMessage
from cryptography.fernet import Fernet


def encrypt_text_pgp(text: str, pub_key: PGPKey) -> str:
    msg = PGPMessage.new(text)
    encrypted = pub_key.encrypt(msg)
    return str(encrypted)


def decrypt_text_pgp(enc_text: str, priv_key: PGPKey) -> str:
    msg = PGPMessage.from_blob(enc_text)
    decrypted = priv_key.decrypt(msg)
    return decrypted.message


def generate_password_key(password: str) -> bytes:
    return Fernet(password.encode('utf-8').ljust(32)[:32])


def encrypt_file(path: Path, pub_key: PGPKey, out_path: Path):
    with open(path, 'rb') as f:
        data = f.read()
    msg = PGPMessage.new(data)
    encrypted = pub_key.encrypt(msg)
    with open(out_path, 'w') as f:
        f.write(str(encrypted))


def decrypt_file(enc_path: Path, priv_key: PGPKey, out_path: Path):
    with open(enc_path, 'r') as f:
        blob = f.read()
    msg = PGPMessage.from_blob(blob)
    decrypted = priv_key.decrypt(msg).message
    with open(out_path, 'wb') as f:
        f.write(decrypted)
