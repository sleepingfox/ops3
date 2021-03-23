from typing import Any

from rest_framework.pagination import LimitOffsetPagination


# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000


class SmallResultsSetPagination(LimitOffsetPagination):


    default_limit = 10
    limit_query_param = ""
    offset_query_param = ""
