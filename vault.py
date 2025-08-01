import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

import click

from commands.note import note
from commands.file import file
from commands.group import group
from commands.key import key
from commands.chat import start_chat
from commands.status import check as status_check
from commands.db import log

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Secure CLI Vault"""
    if ctx.invoked_subcommand is None:
        start_chat()
        ctx.exit()

cli.add_command(note)
cli.add_command(file)
cli.add_command(group)
cli.add_command(key)
cli.add_command(status_check)
cli.add_command(log)

if __name__ == "__main__":
    cli()
