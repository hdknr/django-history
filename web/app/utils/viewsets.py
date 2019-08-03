from collections import OrderedDict
from rest_framework import (pagination, response, exceptions)
from django.core.paginator import InvalidPage


class Pagination(pagination.PageNumberPagination):
    page_size = 30
    max_page_size = 30
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return response.Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_range', list(self.page.paginator.page_range)),
            ('num_pages', self.page.paginator.num_pages),
            ('current_page', self.page.number),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))

    def paginate_queryset(self, queryset, request, view=None):                                                          
        """                                                 
        Paginate a queryset if required, either returning a 
        page object, or `None` if pagination is not configured for this view.                                           
        """                                                 
        page_size = self.get_page_size(request)             
        if not page_size:                                   
            return None                                     

        paginator = self.django_paginator_class(queryset, page_size)                                                    
        page_number = int(request.query_params.get(self.page_query_param, 1))
        if page_number in self.last_page_strings:           
            page_number = paginator.num_pages               
        elif page_number < paginator.page_range.start:
            page_number = paginator.page_range.start 
        elif page_number >= paginator.page_range.stop:
            page_number = paginator.page_range.stop -1 

        try:                                                
            self.page = paginator.page(page_number)         
        except InvalidPage as exc:                          
            msg = self.invalid_page_message.format(         
                page_number=page_number, message=six.text_type(exc)                                                     
            )                                               
            raise exceptions.NotFound(msg)                             

        if paginator.num_pages > 1 and self.template is not None:                                                       
            # The browsable API should display pagination controls.                                                     
            self.display_page_controls = True               

        self.request = request                              
        return list(self.page)                              
