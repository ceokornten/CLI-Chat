import click
from pathlib import Path

from commands.note import create as note_create_cmd, read as note_read_cmd, share as note_share_cmd
from commands.key import list_cmd as key_list_cmd, import_cmd as key_import_cmd, delete_cmd as key_delete_cmd
from commands.group import send_group_message as group_chat_cmd
from commands.db import list_cmd as log_list_cmd

LOG_FILE = Path('logs/chat.log')
LOG_FILE.parent.mkdir(exist_ok=True)


def start_chat():
    """Interactive chat interface."""
    with LOG_FILE.open('a') as log:
        while True:
            click.echo(
                "\n\N{speech balloon} VaultBot: \u0e22\u0e34\u0e19\u0e14\u0e35\u0e15\u0e49\u0e2d\u0e19\u0e23\u0e31\u0e1a! \u0e04\u0e38\u0e13\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e17\u0e33\u0e2d\u0e30\u0e44\u0e23?"
            )
            click.echo(
                "1. \U0001f512 \u0e40\u0e02\u0e49\u0e32\u0e23\u0e2b\u0e31\u0e2a\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\n"
                "2. \U0001f513 \u0e16\u0e2d\u0e14\u0e23\u0e2b\u0e31\u0e2a\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\n"
                "3. \U0001f5dd\ufe0f \u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e01\u0e38\u0e0d\u0e41\u0e08\u0e49\n"
                "4. \U0001f465 \u0e41\u0e0a\u0e23\u0e4c\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e38\u0e48\u0e21\n"
                "5. \U0001f9fe \u0e14\u0e39 log \u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\n"
                "6. \u274c \u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e23\u0e30\u0e1a\u0e1a"
            )
            choice = click.prompt('> ', default='', show_default=False)
            log.write(f"choice:{choice}\n")
            if choice == '1':
                text = click.prompt('\U0001f4dd \u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e40\u0e02\u0e49\u0e32\u0e23\u0e2b\u0e31\u0e2a:')
                note_create_cmd.callback(text)
            elif choice == '2':
                path = click.prompt('\U0001f4c2 \u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e1f\u0e25\u0e4c (note.enc)')
                note_read_cmd.callback(path)
            elif choice == '3':
                click.echo('\n\U0001f5dd\ufe0f \u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e01\u0e38\u0e0d\u0e41\u0e08\u0e49:\n1. \u0e41\u0e2a\u0e14\u0e07\u0e04\u0e35\u0e22\u0e4c\n2. \u0e19\u0e33\u0e40\u0e02\u0e49\u0e32\u0e04\u0e35\u0e22\u0e4c\n3. \u0e25\u0e1a\u0e04\u0e35\u0e22\u0e4c')
                sub = click.prompt('> ', default='', show_default=False)
                if sub == '1':
                    key_list_cmd.callback()
                elif sub == '2':
                    fname = click.prompt('file key')
                    key_import_cmd.callback(fname)
                elif sub == '3':
                    fname = click.prompt('delete key')
                    key_delete_cmd.callback(fname)
            elif choice == '4':
                gname = click.prompt('group name')
                msg = click.prompt('message')
                group_chat_cmd.callback(gname, msg)
            elif choice == '5':
                log_list_cmd.callback(10)
            elif choice == '6':
                click.echo('\U0001f44b bye!')
                break
            else:
                click.echo('invalid choice')
