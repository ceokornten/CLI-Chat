import click

from commands.note import note
from commands.file import file
from commands.group import group
from commands.key import key

@click.group()
def cli():
    """Secure CLI Vault"""
    pass

cli.add_command(note)
cli.add_command(file)
cli.add_command(group)
cli.add_command(key)

if __name__ == "__main__":
    cli()
