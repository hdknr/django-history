from rest_framework import serializers
from .. import models
from app.api.serializers import EndpointField


class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Domain
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    endpoint = EndpointField()
    domain_object = DomainSerializer(source='domain', read_only=True)

    class Meta:
        model = models.Link
        fields = '__all__'
