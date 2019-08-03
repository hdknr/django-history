from django.db import models
from django.urls import reverse
from django.template import Template, Context, loader
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.module_loading import import_string
from functools import reduce
from operator import or_
from . import encoders


def admin_change_url_name(model):
    opt = model._meta
    return f'admin:{opt.app_label}_{opt.model_name}_change'


def admin_change_url(instance):
    return reverse(admin_change_url_name(instance), args=[instance.id])


def slug_query(slug, field_name="slug"):
    keys = [field_name] +  (['id'] if slug.isdigit() else [])
    return reduce(or_, [models.Q(**{i: slug}) for i in keys])


def render(src, request=None, **kwargs):
    return Template(src).render(Context(kwargs))


def render_by(name, request=None, **kwargs):
    return loader.get_template(name).render(context=kwargs)


BASE_DT = timezone.make_aware(parse_datetime('2018-01-01 00:00:00'))


def get_days(now=None, base=None):
    now = now or timezone.now()
    base = base or BASE_DT
    return (now - base).days


def datekey(now=None, salt=None):
    now = now or timezone.localtime(timezone.now())
    salt = salt or now.microsecond
    key = u"{}-{:04x}".format(now.strftime('%y%m%d-%H%M%S'), salt)
    return key


def to_json(obj, class_name=None):
    if isinstance(obj, dict):
        return encoders.to_json(obj)

    ser = class_name and import_string(class_name)
    if ser:
        obj = ser(obj, many=isinstance(obj, (list, models.QuerySet))).data
    return encoders.to_json(obj)