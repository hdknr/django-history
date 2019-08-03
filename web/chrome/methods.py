from django.utils.functional import cached_property
from django.utils import timezone
from urllib.parse import urlparse
from . import utils
# from histories.models import Domain, Link # TODO: delete


class Urls(object):

    @cached_property
    def last_visit_at(self):
        return utils.date_from_webkit(self.last_visit_time)

    @cached_property 
    def parsed_url(self):
        return urlparse(self.url)
    
    @cached_property
    def hostname(self):
        return self.parsed_url.hostname

    @cached_property
    def last_visit_at_aware(self):
        return timezone.make_aware(self.last_visit_at) 

    # TODO: delete
    #     def stock(self, enabled=True):
    #         return Domain.objects.stock_link(
    #             url=self.url,
    #             title=self.title,
    #             visited_at=self.last_visit_at_aware, 
    #             enabled=enabled)

    # TODO: delete
    # @cached_property
    # def is_stocked(self):
    #     return Link.objects.filter(url=self.url, enabled=True).exists()

    @cached_property
    def markdown(self):
        return f"[{self.title}]({self.url})"
