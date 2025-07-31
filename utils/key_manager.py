from pathlib import Path
from pgpy import PGPKey, PGPUID
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm

KEY_DIR = Path('keys')
PUBLIC_KEY_FILE = KEY_DIR / 'public.asc'
PRIVATE_KEY_FILE = KEY_DIR / 'private.asc'

KEY_DIR.mkdir(exist_ok=True)

def generate_keypair(name: str, email: str, passphrase: str):
    key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 2048)
    uid = PGPUID.new(name, email=email)
    key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications}, hashes=[HashAlgorithm.SHA256])
    with open(PRIVATE_KEY_FILE, 'w') as f:
        f.write(str(key))
    with open(PUBLIC_KEY_FILE, 'w') as f:
        f.write(str(key.pubkey))


def load_default_pubkey():
    if not PUBLIC_KEY_FILE.exists():
        raise FileNotFoundError('No public key found; generate one with generate-keypair')
    return PGPKey.from_file(PUBLIC_KEY_FILE)[0]


def load_default_privkey():
    if not PRIVATE_KEY_FILE.exists():
        raise FileNotFoundError('No private key found; generate one with generate-keypair')
    return PGPKey.from_file(PRIVATE_KEY_FILE)[0]
