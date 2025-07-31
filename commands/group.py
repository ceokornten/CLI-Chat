import click

@click.group()
def group():
    """Manage groups (placeholder)"""
    pass


@group.command('create')
@click.argument('name')
def create_group(name):
    click.echo(f'Group {name} created (not implemented)')
