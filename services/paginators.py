from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size = 40

    def get_paginated_response(self, data):
        return Response({
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'num_pages': self.page.paginator.num_pages,
            'results': data,
        })


# todo: add ordering for pagination on some models

class MyPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'per_page'

    def get_paginated_response(self, data):
        return Response({
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'num_pages': self.page.paginator.num_pages,
            'results': data,
        })
