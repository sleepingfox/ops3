from rest_framework import viewsets
from rest_framework.decorators import action
from apps.assets.status_code.status import *

from apps.assets.serializers.serializers import *
from apps.assets.models import *
from apps.assets.serializers.idc_serializers import IdcSerializer
from rest_framework import response
# from .utils.myfilter import MyFilter
# class UserViewSet(viewsets.ModelViewSet):
# class UserViewSet(generics.GenericAPIView):
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class IdcViewSet(viewsets.ModelViewSet):
    queryset = Idc.objects.all()

    serializer_class = IdcSerializer
