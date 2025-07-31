from pathlib import Path
from pgpy import PGPKey, PGPUID
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm

KEY_DIR = Path('keys')
KEY_DIR.mkdir(exist_ok=True)


def generate_keypair(name: str, email: str, passphrase: str):
    key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 2048)
    uid = PGPUID.new(name, email=email)
    key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications}, hashes=[HashAlgorithm.SHA256])
    priv_path = KEY_DIR / f'{email}_private.asc'
    pub_path = KEY_DIR / f'{email}_public.asc'
    with open(priv_path, 'w') as f:
        f.write(str(key))
    with open(pub_path, 'w') as f:
        f.write(str(key.pubkey))
    return priv_path, pub_path


def import_key(path: Path) -> PGPKey:
    with open(path, 'r') as f:
        key, _ = PGPKey.from_blob(f.read())
    return key
