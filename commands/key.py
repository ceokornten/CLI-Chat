import click
from utils.key_manager import generate_keypair

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
    click.echo('Keypair generated in keys/')
