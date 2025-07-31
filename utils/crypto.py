from __future__ import annotations

from typing import Optional

from cryptography.fernet import Fernet
from pgpy import PGPKey, PGPMessage
from pgpy.constants import SymmetricKeyAlgorithm, CompressionAlgorithm


def encrypt_text(text: str, *, pubkey: Optional[PGPKey] = None, password: Optional[str] = None) -> bytes:
    if pubkey:
        message = PGPMessage.new(text)
        enc = pubkey.encrypt(
            message,
            cipher=SymmetricKeyAlgorithm.AES256,
            compression=CompressionAlgorithm.ZLIB,
        )
        return bytes(str(enc), "utf-8")
    elif password:
        f = Fernet(password.encode())
        return f.encrypt(text.encode())
    else:
        raise ValueError("Need pubkey or password")


def decrypt_text(data: bytes, *, privkey: Optional[PGPKey] = None, password: Optional[str] = None) -> str:
    if privkey:
        encrypted_message = PGPMessage.from_blob(data.decode("utf-8"))
        dec = privkey.decrypt(encrypted_message)
        return dec.message
    elif password:
        f = Fernet(password.encode())
        return f.decrypt(data).decode()
    else:
        raise ValueError('Need privkey or password')
