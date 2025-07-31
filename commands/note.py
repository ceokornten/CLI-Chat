import click
from pathlib import Path
from utils import key_manager, crypto, config

NOTES_DIR = Path('notes')
NOTES_DIR.mkdir(exist_ok=True)

@click.group()
def note():
    """Manage encrypted notes"""
    pass


@note.command()
@click.argument('title')
@click.option('--message', prompt=True)
@click.option('--key', type=click.Path(exists=True), required=True, help='Recipient public key')
def create(title, message, key):
    pub_key = key_manager.import_key(Path(key))
    encrypted = crypto.encrypt_text_pgp(message, pub_key)
    path = NOTES_DIR / f'{title}.asc'
    with open(path, 'w') as f:
        f.write(encrypted)
    click.echo(f'Note saved to {path}')


@note.command()
@click.argument('title')
@click.option('--key', type=click.Path(exists=True), required=True, help='Private key to decrypt')
def read(title, key):
    priv_key = key_manager.import_key(Path(key))
    path = NOTES_DIR / f'{title}.asc'
    if not path.exists():
        click.echo('Note not found')
        return
    with open(path) as f:
        data = f.read()
    text = crypto.decrypt_text_pgp(data, priv_key)
    click.echo(text)


@note.command()
def list():
    for f in NOTES_DIR.glob('*.asc'):
        click.echo(f.stem)
