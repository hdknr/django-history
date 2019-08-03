from django.contrib.sitemaps import Sitemap, views
from django.urls import path, re_path, reverse


class AppSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['about', 'home']

    def location(self, name):
        names = ['about', 'home']
        return reverse('pages_page_detail', kwargs={'name': name}) 

sitemap = AppSitemap()