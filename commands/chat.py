import click
from pathlib import Path

from commands.note import create as note_create_cmd, read as note_read_cmd, share as note_share_cmd
from commands.key import list_cmd as key_list_cmd, import_cmd as key_import_cmd, delete_cmd as key_delete_cmd
from commands.status import check as status_check_cmd

LOG_FILE = Path('logs/chat.log')
LOG_FILE.parent.mkdir(exist_ok=True)


def start_chat():
    """Interactive chat interface."""
    with LOG_FILE.open('a') as log:
        while True:
            click.echo(
                "\n\N{speech balloon} VaultBot: \u0e2a\u0e27\u0e31\u0e2a\u0e14\u0e35\u0e04\u0e23\u0e31\u0e1a \u0e2a\u0e39\u0e48\u0e23\u0e30\u0e1a\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e25\u0e31\u0e1a\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e25\u0e31\u0e1a"
            )
            click.echo(
                "1. \U0001f512 \u0e40\u0e02\u0e49\u0e32\u0e23\u0e2b\u0e31\u0e2a\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\n"
                "2. \U0001f513 \u0e16\u0e2d\u0e14\u0e23\u0e2b\u0e31\u0e2a\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\n"
                "3. \U0001f5dd\ufe0f \u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e01\u0e38\u0e0d\u0e41\u0e08\u0e49\n"
                "4. \U0001f465 \u0e41\u0e0a\u0e23\u0e4c\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e21\n"
                "5. \U0001f50d \u0e15\u0e23\u0e27\u0e08\u0e2a\u0e16\u0e32\u0e19\u0e30\n"
                "6. \u274c \u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e23\u0e30\u0e1a\u0e1a"
            )
            choice = click.prompt('> ', default='', show_default=False)
            log.write(f"choice:{choice}\n")
            if choice == '1':
                text = click.prompt('\U0001f4dd \u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e40\u0e02\u0e49\u0e32\u0e23\u0e2b\u0e31\u0e2a:')
                note_create_cmd.callback(text)
            elif choice == '2':
                path = click.prompt('\U0001f4c2 \u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e1f\u0e25\u0e4c (\u0e40\u0e0a\u0e48\u0e19: note.enc) \u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e16\u0e2d\u0e14\u0e23\u0e2b\u0e31\u0e2a:')
                note_read_cmd.callback(path)
            elif choice == '3':
                click.echo(
                    '\n\U0001f5dd\ufe0f \u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e01\u0e38\u0e0d\u0e41\u0e08\u0e49:\n'
                    '1. \u0e41\u0e2a\u0e14\u0e07\u0e04\u0e35\u0e22\u0e4c\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\n'
                    '2. \u0e19\u0e33\u0e40\u0e02\u0e49\u0e32\u0e04\u0e35\u0e22\u0e4c\u0e43\u0e2b\u0e21\u0e48\n'
                    '3. \u0e25\u0e1a\u0e04\u0e35\u0e22\u0e4c'
                )
                sub = click.prompt('> ', default='', show_default=False)
                log.write(f"key_action:{sub}\n")
                if sub == '1':
                    key_list_cmd.callback()
                elif sub == '2':
                    fname = click.prompt('\U0001f4c1 \u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e1f\u0e25\u0e4c key \u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e19\u0e33\u0e40\u0e02\u0e49\u0e32:')
                    key_import_cmd.callback(fname)
                elif sub == '3':
                    fname = click.prompt('\U0001f5d1\ufe0f \u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e0a\u0e37\u0e48\u0e2d key \u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e25\u0e1a:')
                    key_delete_cmd.callback(fname)
            elif choice == '4':
                recips = click.prompt('\U0001f465 \u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e1f\u0e25\u0e4c key \u0e1c\u0e39\u0e49\u0e23\u0e31\u0e1a').split()
                text = click.prompt('\U0001f4dd \u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21')
                note_share_cmd.callback(text, recips)
            elif choice == '5':
                status_check_cmd.callback()
            elif choice == '6':
                click.echo('\U0001f44b \u0e02\u0e2d\u0e1a\u0e04\u0e38\u0e13\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49 VaultBot \u2014 \u0e25\u0e32\u0e01\u0e48\u0e2d\u0e19!')
                break
            else:
                click.echo('\u0e44\u0e21\u0e48\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07')
