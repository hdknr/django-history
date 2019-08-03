from django.contrib.sitemaps import Sitemap, views
from django.urls import path, re_path, reverse


class AppSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        from histories.models import Note
        return Note.objects.all()

sitemap = AppSitemap()