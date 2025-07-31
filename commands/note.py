import click
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
