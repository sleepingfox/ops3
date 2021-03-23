# # import django_filters

from django.middleware.csrf import CsrfViewMiddleware
# # from django_filters.rest_framework import FilterSet
# from rest_framework import filters
#
# from assets.models import Host
#
#
# class MyFilter(FilterSet):
#
#         '''
#         单条件检索
#         :param view:
#         :param request:
#         :return:
#         '''
#         res = django_filters.CharFilter(hostname="test",lookup_expr="icontains")
#         print("3333333")
#         # print(request.query_params)
#         class Meta:
#             model = Host
#             fields = ["hostname"]
#
#
#
from django.contrib.auth.middleware import AuthenticationMiddleware
