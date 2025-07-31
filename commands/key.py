import click
from utils.key_manager import (
    generate_keypair,
    backup_key,
    PUBLIC_KEY_FILE,
    PRIVATE_KEY_FILE,
)

@click.group()
def key():
    """PGP Key management"""
    pass

@key.command('generate')
@click.option('--name', prompt=True)
@click.option('--email', prompt=True)
@click.option('--passphrase', prompt=True, hide_input=True, confirmation_prompt=True)
def generate_key(name, email, passphrase):
    generate_keypair(name, email, passphrase)
    backup_key(PUBLIC_KEY_FILE)
    backup_key(PRIVATE_KEY_FILE)
    click.echo('Keypair generated in keys/')


def list_keys():
    import os
    for k in os.listdir('keys'):
        if k.endswith('.asc'):
            print(k)


def import_key(filename):
    import shutil
    shutil.copy(filename, 'keys/')


def delete_key(filename):
    import os
    os.remove(f'keys/{filename}')


@key.command('list')
def list_cmd():
    """List available keys"""
    list_keys()


@key.command('import')
@click.argument('filename', type=click.Path(exists=True))
def import_cmd(filename):
    """Import a key file into the keys directory"""
    import_key(filename)
    click.echo('Key imported')


@key.command('delete')
@click.argument('filename')
def delete_cmd(filename):
    """Delete a key from the keys directory"""
    delete_key(filename)
    click.echo('Key deleted')
