'''
https://django-filter.readthedocs.io/en/master/
'''
import django_filters
from .. import models


class LinkFilter(django_filters.FilterSet):
    domain_name =  django_filters.CharFilter(field_name='domain', lookup_expr='hostname__icontains')

    class Meta:
        model = models.Link
        exclude = ['tags']