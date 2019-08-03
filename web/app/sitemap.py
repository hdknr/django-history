from django.contrib.sitemaps import Sitemap, views
from django.urls import path, re_path, reverse
from django.utils.module_loading import import_module


def get_sitemap(app):
    try:
        return getattr(import_module(f"{app}.sitemap"), 'sitemap', None)
    except:
        pass


apps = ['histories', 'pages', 'chrome', ]
_maps = ((app, get_sitemap(app)) for app in apps)
sitemaps = dict(i for i in _maps if i[1])


urlpatterns = [
    path('sitemap.xml', views.sitemap, {'sitemaps': sitemaps}),
    re_path('^sitemap-(?P<section>.+).xml', views.sitemap, {'sitemaps': sitemaps}),
]