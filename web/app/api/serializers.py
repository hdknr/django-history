from django.urls import reverse
from rest_framework import fields, serializers
import traceback


def drf_endpoint(instance, url_name=None, pk_name='pk'):
    ''' DRF endpoint '''
    try:
        if hasattr(instance, 'get_endpoint_url'):
            return instance.get_endpoint_url()
        name = url_name or f"{instance._meta.model_name}-detail"
        return reverse(name, kwargs={pk_name: instance.pk})
    except:
        pass
    return ''


class EndpointField(fields.Field):

    def __init__(self, **kwargs):
        kwargs['source'] = '*'
        kwargs['read_only'] = True
        self.url_name = kwargs.get('url_name', None)
        self.attr_name = kwargs.get('attr_name', None)
        super().__init__(**kwargs) 

    def get_url_name(self, value):
        return self.url_name

    def to_representation(self, value):
        instance = self.attr_name and getattr(value, self.attr_name, None) or value
        url = drf_endpoint(instance, url_name=self.get_url_name(value))
        request = self.context.get('request', None)
        return (request and url ) and request.build_absolute_uri(url) or url or None


class BaseModelSerializer(serializers.ModelSerializer):
    endpoint = EndpointField()