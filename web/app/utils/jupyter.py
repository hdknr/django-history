from IPython.core.display import display, HTML
from app.utils import render_by


def _html(src):
    display(HTML(src))


def html(queryset):
    opt = queryset.model._meta
    template = f'jupyter/{opt.app_label}/{opt.model_name}.html'
    _html(render_by(template, qs=queryset))
