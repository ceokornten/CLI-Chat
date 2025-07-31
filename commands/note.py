import click
from pgpy import PGPKey, PGPMessage
from utils.crypto import encrypt_text, decrypt_text
from utils.key_manager import load_default_pubkey, load_default_privkey

@click.group()
def note():
    """Manage encrypted notes"""
    pass

@note.command()
@click.argument('text')
def create(text):
    """Encrypt and store a note locally"""
    pubkey = load_default_pubkey()
    ciphertext = encrypt_text(text, pubkey=pubkey)
    with open('note.enc', 'wb') as f:
        f.write(ciphertext)
    click.echo('Note encrypted and saved to note.enc')

@note.command()
@click.argument('path', type=click.Path(exists=True))
def read(path):
    """Decrypt a local encrypted note"""
    privkey = load_default_privkey()
    with open(path, 'rb') as f:
        data = f.read()
    plaintext = decrypt_text(data, privkey=privkey)
    click.echo(plaintext)


def share_note(text, recipient_keys):
    from pgpy.constants import SymmetricKeyAlgorithm, CompressionAlgorithm
    message = PGPMessage.new(text)
    enc_message = None
    for keyfile in recipient_keys:
        with open(f'keys/{keyfile}', 'r') as f:
            pubkey, _ = PGPKey.from_blob(f.read())
        if enc_message is None:
            enc_message = pubkey.encrypt(
                message,
                cipher=SymmetricKeyAlgorithm.AES256,
                compression=CompressionAlgorithm.ZLIB,
            )
        else:
            enc_message |= pubkey.encrypt(message)
    with open('note.enc', 'w') as f:
        f.write(str(enc_message))


@note.command()
@click.argument('text')
@click.option('--recipients', multiple=True, required=True)
def share(text, recipients):
    """Encrypt note for multiple recipients"""
    share_note(text, recipients)
    click.echo('Note shared and saved to note.enc')
