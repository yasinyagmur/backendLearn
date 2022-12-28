from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'sayfa'


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'adet'
    offset_query_param = 'baslangic'
