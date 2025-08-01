from datetime import datetime
from typing import Optional
import click

from utils.db_conn import get_collection

COLL = get_collection()


def log_encrypted_note(encrypted_text: str, *, group: Optional[str] = None, sender: Optional[str] = None, command: str = "note.create", status: str = "ok"):
    doc = {
        "timestamp": datetime.utcnow().isoformat(),
        "group": group,
        "sender": sender,
        "encrypted_text": encrypted_text,
        "command": command,
        "status": status,
    }
    try:
        COLL.insert_one(doc)
    except Exception:
        pass


def log_event(command: str, status: str = "ok"):
    doc = {
        "timestamp": datetime.utcnow().isoformat(),
        "command": command,
        "status": status,
    }
    try:
        COLL.insert_one(doc)
    except Exception:
        pass


@click.group()
def log():
    """View encrypted logs"""
    pass


@log.command('view')
@click.option('--group')
def view_cmd(group):
    """View logs for a specific group"""
    query = {"group": group} if group else {}
    try:
        for entry in COLL.find(query).sort("timestamp"):
            click.echo(entry)
    except Exception:
        click.echo('No database connection')


@log.command('list')
@click.option('--last', type=int, default=10)
def list_cmd(last):
    """Show the latest N logs"""
    try:
        for entry in COLL.find().sort("timestamp", -1).limit(last):
            click.echo(entry)
    except Exception:
        click.echo('No database connection')


@log.command('full')
def full_cmd():
    """Display all logs"""
    try:
        for entry in COLL.find().sort("timestamp"):
            click.echo(entry)
    except Exception:
        click.echo('No database connection')
