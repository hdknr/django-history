from django.db import models
from datetime import datetime, time, timedelta
from histories.models import Ignore, Domain, Link
from . import utils


class UrlsQuerySet(models.QuerySet):

    def daterange(self, dt_from=None, dt_to=None, **kwargs):
        dt_from = dt_from or datetime.combine(
            datetime.now().date(), time(0, 0, 0))
        dt_to = dt_to or datetime.combine(
            datetime.now().date(), time(23, 59, 59))
        dt_from = utils.date_to_webkit(dt_from) 
        dt_to = utils.date_to_webkit(dt_to) 
        return self.filter(
            last_visit_time__gte=dt_from,
            last_visit_time__lte=dt_to, **kwargs)

    def day_before(self, days=0):
        dt_from = datetime.combine(datetime.now().date(), time(0, 0, 0))
        dt_to = dt_from + timedelta(days=1)
        dt_from = dt_from - timedelta(days=days)
        dt_to = dt_to - timedelta(days=days)
        return self.daterange(dt_from, dt_to)

    def remove_ignores(self):
        # TODO: move to historis.Ignore.objects

        for i in Ignore.objects.filter(is_domain=True):
            self.filter(url__iregex=r'^https?://' + i.pattern + r'[:/]').delete()
        for i in Ignore.objects.filter(is_domain=False):
            self.filter(url__iregex=i.pattern).delete()

    def remove_stocked(self):
        # TODO: move to historis.Link.objects
        for link in Link.objects.all():
            clink = self.filter(url=link.url).first()
            if not clink:
                continue

            if not link.title:
                link.title = clink.title
                link.save()
            clink.delete()
        
    def update_domain(self):
        # TODO: move to historis.Domain.objects

        for i in self.all():
            Domain.objects.get_or_create(hostname=i.parsed_url.hostname)


    def stock(self, dt_from=None, dt_to=None):
        # TODO: move to historis.Domain.objects
        for domain in Domain.objects.filter(stock=True):
            self.stock_for(domain, dt_from=dt_from, dt_to=dt_to)

    def stock_for(self, domain, dt_from=None, dt_to=None):
        # TODO: move to historis.Domain.objects
        for url in self.daterange(
            dt_from=dt_from, dt_to=dt_to,
            url__iregex=r'^https?://' + domain.hostname + r'[:/]'
        ):
            if 1 > domain.link_set.filter(url=url.url).update(title=url.title, visited_at=url.last_visit_at):
                domain.link_set.create(url=url.url, title=url.title, visited_at=url.last_visit_at)
            url.delete()