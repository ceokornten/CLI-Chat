import click
import json
import shutil
from datetime import datetime
from pathlib import Path
from pgpy import PGPKey, PGPMessage
from pgpy.constants import SymmetricKeyAlgorithm, CompressionAlgorithm

GROUP_DIR = Path('groups')
GROUP_DIR.mkdir(exist_ok=True)

def _group_path(name: str) -> Path:
    path = GROUP_DIR / name
    (path / 'messages').mkdir(parents=True, exist_ok=True)
    return path

@click.group()
def group():
    """Manage groups"""
    pass

@group.command('create')
@click.argument('name')
def create_group(name):
    """Create a new group"""
    gpath = _group_path(name)
    members_file = gpath / 'members.json'
    if members_file.exists():
        click.echo('Group already exists')
        return
    members_file.write_text('[]')
    click.echo(f'Group {name} created')


@group.command('add-member')
@click.argument('group_name')
@click.argument('key_file', type=click.Path(exists=True))
def add_member(group_name, key_file):
    """Add a member to a group"""
    gpath = _group_path(group_name)
    members_file = gpath / 'members.json'
    if not members_file.exists():
        click.echo('Group does not exist')
        return
    members = json.loads(members_file.read_text())
    key_name = Path(key_file).name
    dest = Path('keys') / key_name
    if not dest.exists():
        shutil.copy(key_file, dest)
    if key_name not in members:
        members.append(key_name)
        members_file.write_text(json.dumps(members))
        click.echo(f'Added {key_name} to {group_name}')
    else:
        click.echo('Member already exists')


@group.command('members')
@click.argument('group_name')
def list_members(group_name):
    """List group members"""
    gpath = _group_path(group_name)
    members_file = gpath / 'members.json'
    if not members_file.exists():
        click.echo('Group does not exist')
        return
    members = json.loads(members_file.read_text())
    for m in members:
        click.echo(m)


@group.command('chat')
@click.argument('group_name')
@click.option('--message', prompt=True)
def send_group_message(group_name, message):
    """Encrypt and store a group message"""
    gpath = _group_path(group_name)
    members_file = gpath / 'members.json'
    if not members_file.exists():
        click.echo('Group does not exist')
        return
    members = json.loads(members_file.read_text())
    if not members:
        click.echo('No members in group')
        return
    keys = []
    for m in members:
        pub, _ = PGPKey.from_file(Path('keys') / m)
        keys.append(pub)
    msg = PGPMessage.new(message)
    enc_msg = None
    for pub in keys:
        if enc_msg is None:
            enc_msg = pub.encrypt(msg, cipher=SymmetricKeyAlgorithm.AES256, compression=CompressionAlgorithm.ZLIB)
        else:
            enc_msg |= pub.encrypt(msg)
    ts = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    out_file = gpath / 'messages' / f'{ts}.asc'
    out_file.write_text(str(enc_msg))
    click.echo(f'Message stored in {out_file}')
