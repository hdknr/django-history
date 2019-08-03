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
@click.option('--date', '-d', default=None)
@click.pass_context
def for_day(ctx, date):
    ''' Links for a Day'''
    date = date and datetime.strptime(date, '%Y-%m-%d').date() \
        or datetime.now().date()
    for link in models.Link.objects.filter(updated_at__date=date).order_by('-updated_at'):
        click.echo(f"- {link.markdown}")


def get_chrome_link(url):
    from chrome.clonedb import clonedb
    from chrome.models import Urls

    clonedb()

    return Urls.objects.filter(url=url).first()


@main.command()
@click.argument('url')
@click.argument('tags', nargs=-1)
@click.pass_context
def md_chrome(ctx, url, tags):
    '''Chrome URL'''

    link =  get_chrome_link(url)
    history = models.Domain.objects.stock_link(
        url=link.url,
        title=link.title,
        visited_at=link.last_visit_at_aware, 
        enabled=True)

    if tags:
        history.tags.add(*tags)

    click.echo(link.markdown)
