from rest_framework import viewsets
from . import serializers, filters, permissions
from .. import models
from app.api.paginations import Pagination


class LinkViewSet(viewsets.ModelViewSet):
    """
    """
    permission_classes = [permissions.Permission, ]
    filter_class = filters.LinkFilter
    serializer_class = serializers.LinkSerializer
    queryset = models.Link.objects.all()
    pagination_class = type('LinkPagination', (Pagination,), {'page_size': 30})
