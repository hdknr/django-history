import djclick as click
from django.db.models import Q
from django.utils import translation
from datetime import datetime, timedelta, time
from chrome import models
from logging import getLogger
log = getLogger()

translation.activate('ja')


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.pass_context
def clonedb(ctx):
    '''Simpley Copy Chrome Database'''
    from chrome.clonedb import clonedb
    clonedb()


@main.command()
@click.option('--date', '-d', default=None)
@click.pass_context
def for_day(ctx, date):
    ''' Links for a Day'''
    date = date and datetime.strptime(date, '%Y-%m-%d').date() \
        or datetime.now().date()
    query = dict(
        dt_from=datetime.combine(date, time(0, 0, 0)),
        dt_to=datetime.combine(date + timedelta(days=1), time(0, 0, 0)),
    )

    for url in models.Urls.objects.daterange(**query):
        click.echo(f"- {url.markdown}")

# TODO: move following commands to hisotries

@main.command()
@click.option('--backdays', '-b', default=0)
@click.pass_context
def stock(ctx, backdays):
    '''Stock Link for Domain(stock=True)'''
    from chrome.clonedb import clonedb
    clonedb()

    kwargs = {}
    if backdays >= 0:
        kwargs['dt_from'] = datetime.combine(
            (datetime.now() - timedelta(days=backdays)).date(),
            time(0, 0, 0))

    models.Urls.objects.remove_ignores()
    models.Urls.objects.remove_stocked()
    #
    models.Urls.objects.stock(**kwargs)


@main.command()
@click.pass_context
def remove_stocked(ctx):
    '''Remove if stocked'''
    models.Urls.objects.remove_stocked()
