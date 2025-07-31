import click
from commands.note import note
from commands.file import file
from commands.group import group

@click.group()
def cli():
    """Secure Vault CLI"""
    pass

cli.add_command(note)
cli.add_command(file)
cli.add_command(group)

if __name__ == '__main__':
    cli()
