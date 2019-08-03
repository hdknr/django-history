from collections import OrderedDict
from rest_framework import (pagination, response)


class Pagination(pagination.PageNumberPagination):
    page_size = 16
    max_page_size = 200 
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return response.Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_range', list(self.page.paginator.page_range)),
            ('current_page', self.page.number),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
