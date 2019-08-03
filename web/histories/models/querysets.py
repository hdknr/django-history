from django.db import models
from datetime import datetime, time, timedelta
from urllib.parse import urlparse


class DomainQuerySet(models.QuerySet):

    def get_for_link(self, url):
        # Link fields: title, visited_at, enabled=True
        u = urlparse(url)
        obj, created = self.get_or_create(hostname=u.hostname)
        return obj

    def stock_link(self, url, **fields):            
        # Link fields: title, visited_at, enabled=True
        u = urlparse(url)
        obj = self.get_for_link(url)

        if 1 > obj.link_set.filter(url=url).update(**fields):
            return obj.link_set.create(url=url, **fields)
        return obj.link_set.filter(url=url).first()