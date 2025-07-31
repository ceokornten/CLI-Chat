import click
from pathlib import Path
from utils import key_manager, crypto

FILES_DIR = Path('files')
FILES_DIR.mkdir(exist_ok=True)

@click.group()
def file():
    """Manage encrypted files"""
    pass


@file.command('upload')
@click.argument('filepath', type=click.Path(exists=True))
@click.option('--key', type=click.Path(exists=True), required=True, help='Recipient public key')
def upload(filepath, key):
    pub_key = key_manager.import_key(Path(key))
    src = Path(filepath)
    dest = FILES_DIR / f'{src.name}.asc'
    crypto.encrypt_file(src, pub_key, dest)
    click.echo(f'Encrypted file saved to {dest}')


@file.command('download')
@click.argument('encfile', type=click.Path(exists=True))
@click.option('--key', type=click.Path(exists=True), required=True, help='Private key')
@click.option('--out', type=click.Path(), required=True)
def download(encfile, key, out):
    priv_key = key_manager.import_key(Path(key))
    crypto.decrypt_file(Path(encfile), priv_key, Path(out))
    click.echo(f'Decrypted file written to {out}')


@file.command('list')
def list_files():
    for f in FILES_DIR.glob('*.asc'):
        click.echo(f.name)
