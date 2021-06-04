from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework.response import Response
# from .utils.myfilter import MyFilter
# class UserViewSet(viewsets.ModelViewSet):
# class UserViewSet(generics.GenericAPIView):
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from apps.assets.utils.pageUtil import pageUtil
from apps.assets.utils.sortByUtil import  sortByUtil
from apps.common import tokenUtils
from ops3 import settings

from .serializers.serializers import *

from rest_framework_jwt.views import *

from rest_framework_jwt.settings import api_settings
from apps.common.status_code import status
from apps.common.auth.myauth import myauth
import datetime



class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    """
    API endpoint that allows users to be viewed or edited.
    """

    authentication_classes = [myauth]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]
    # def retrieve(self,request):
    #     print(request)
    #     print('retrieve')
    #
    #     return {"ok"}

    # def list(self, request, *args, **kwargs):
    #     serializers = self.get_serializer()
    #
    #
    #     query = self.get_queryset()
    #
    #     print("222222222")
    #     print(request.session)
    #
    #     print(request.user)
    #     print(kwargs)
    #
    #     self.get_permissions()
    #
    #     return Response(serializers.data)


    # def login(self,request):
    #     print("zzzzzzzzzzzzzzzzzzz")
    #     info_dic = request.data
    #     username= info_dic.get("username")
    #     print(username)
    #     print(info_dic)
    #     # obj = User.objects.filter(username=username).first()
    #
    #
    #
    #
    #
    #     print("obj")
    #     print(info_dic["password"])
    #     # print(obj.password)
    #     # print(info_dic[username])
    #
    #
    #     user =authenticate(username=username,password=info_dic["password"])
    #
    #
    #     if user:
    #
    #
    #
    #         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    #         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    #
    #         payload = jwt_payload_handler(user)
    #         token = jwt_encode_handler(payload)
    #
    #
    #
    #         print("token")
    #         print("tttttttttttt")
    #         print(token)
    #
    #         print(user.id)
    #         #更新操作，登陆一次生成一个token
    #         Token.objects.filter(user_id=user.id).delete()
    #         Token.objects.create(user=user,key=token)
    #
    #         import json
    #         #判断密码是否正确
    #         return Response(data={"message": "登录成功", "status": status.HTTP_200_OK, "result": {"token":token,"user":{"username":user.username}}})
    #
    #     return Response(data={"message": "登陆失败", "status": status.HTTP_404_NOT_FOUND, "result": {}})


class Login(APIView):

    def post(self, request):

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

        print("@@@@@@@@@2")
        user = authenticate(username=username, password=info_dic["password"])


        if user:


            access_exp  = datetime.datetime.utcnow()+datetime.timedelta(seconds=settings.JWT_EXP_SEC)
            access_iat = datetime.datetime.utcnow()

            access_payload =  tokenUtils.GetToken().jwt_set_payload(dic={"user":user.id},token_type="JWT_PAYLOAD",exp=access_exp,iat=access_iat)


            refresh_exp  = datetime.datetime.utcnow()+datetime.timedelta(seconds=settings.JWT_AIT_SEC)
            refresh_iat = datetime.datetime.utcnow()


            refresh_payload =  tokenUtils.GetToken().jwt_set_payload(dic={"user":user.id},token_type="JWT_REFRESH_PAYLOAD",exp=refresh_exp,iat=refresh_iat)

            print("login")
            # print(payload["iat"])
            # print(payload["exp"])

            access_token = tokenUtils.GetToken().get_token(access_payload)
            refresh_token = tokenUtils.GetToken().get_token(refresh_payload)







            import json
            # 判断密码是否正确
            return Response(data={"message": "登录成功", "status": status.HTTP_200_OK,
                                  "result": {"refresh_token":refresh_token,"access_token": access_token, "user": { "username": user.username}}})

        return Response(data={"message": "登陆失败", "status": status.HTTP_404_NOT_FOUND, "result": {}})



