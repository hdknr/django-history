from IPython.core.display import display, HTML
from . import models
from app.utils.jupyter import html
from app.utils.encoders import to_json


def domain(qs=None, stock=True, **query):
    qs = qs or models.Domain.objects
    return qs.filter(stock=stock, **query)


def link(qs=None, enabled=True, **query):
    qs = qs or models.Link.objects
    return qs.filter(enabled=enabled, **query)


def ignore(qs=None, **query):
    qs = qs or models.Ignore.objects
    return qs.filter(**query).order_by('-is_domain', 'pattern')