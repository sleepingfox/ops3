from rest_framework import viewsets
from rest_framework.decorators import action

from apps.assets.serializers.cabinet_serializers import CabinetSerializer
from apps.assets.status_code.status import *

from apps.assets.serializers.serializers import *
from apps.assets.models import *
from rest_framework import response
# from .utils.myfilter import MyFilter
# class UserViewSet(viewsets.ModelViewSet):
# class UserViewSet(generics.GenericAPIView):
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


from rest_framework.response import Response
from apps.assets.status_code.status import *
from apps.common.auth.myauth import myauth


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()

    serializer_class = CabinetSerializer

    authentication_classes = [myauth]


    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        data = self.get_serializer(queryset,many=True).data
        return Response(data = {"data":data,"status":HTTP_200_OK,"msg":"成功"})
