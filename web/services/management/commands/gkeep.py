import djclick as click
from django.db.models import Q
from django.utils import translation, timezone
from datetime import datetime, timedelta, time
from histories import models
from logging import getLogger
log = getLogger()

translation.activate('ja')


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.argument('query')
@click.pass_context
def note_list(ctx, query):
    ''' List of Note'''

    import gkeepapi
    keep = gkeepapi.Keep()
    keep.login(user, password)
    gnotes = keep.find(query=query)
    for note in gnotes:
        click.note(note.title)