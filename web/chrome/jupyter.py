from IPython.core.display import display, HTML
from . import models
from app.utils.jupyter import html      # NOQA
from app.utils.encoders import to_json
from datetime import datetime, time, timedelta

def remove_ignores():
    models.Urls.objects.remove_ignores()


def urls(qs=None, **kwargs):
    qs = qs or models.Urls.objects
    return qs.filter(**kwargs)


def day(datestr=None):
    kwargs = {}
    if datestr:
        kwargs['dt_from'] = datetime.combine(
            datetime.strptime(datestr, '%Y-%m-%d').date(),
            time(0, 0, 0))
        kwargs['dt_to'] = kwargs['dt_from'] + timedelta(days=1)
    return models.Urls.objects.daterange(**kwargs).order_by('-last_visit_time')