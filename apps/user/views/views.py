from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from django.contrib.auth.models import User
from ..serializers import serializers
from django.urls import path
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from apps.common.status_code import status

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer




class AuthUserView(ModelViewSet):

    # @action(methods=['post'], detail=False)
    def login(self, request):
        print("zzzzzzzzzzzzzzzzzzz")
        info_dic = request.data
        username = info_dic.get("username")
        print(username)
        print(info_dic)
        # obj = User.objects.filter(username=username).first()

        print("obj")
        print(info_dic["password"])
        # print(obj.password)
        # print(info_dic[username])
        user = authenticate(username=username, password=info_dic["password"])
        if user:
            print(user.id)
            # 更新操作，登陆一次生成一个token
            Token.objects.filter(user_id=user.id).delete()
            token = Token.objects.create(user=user)

            # 判断密码是否正确
            return Response(data={"message": "登录成功", "status": status.HTTP_200_OK,
                                           "result": {"token": token.key, "user": {"username": user.username}}})

        return Response(data={"message": "登陆失败", "status": status.HTTP_404_NOT_FOUND, "result": {}})
