from django.http import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin

from rest_framework.authtoken.models import Token
from rest_framework import authtoken
import time
from cmdb.status_code.status import *
from ops3 import settings

class InterceptorMiddleware(MiddlewareMixin):


    def   process_request(self,request):

        print("token_control")
        token = request.META.get("HTTP_AUTHORIZATION")
        print(token)
        print(request.META.get("PATH_INFO"))

        if_login = request.META.get("PATH_INFO")

        token_create = Token.objects.filter(key=token).first()

        if not token_create and if_login != "/users/login/":

            return JsonResponse({"status":HTTP_401_UNAUTHORIZED,"result": {"token": ""}})



        if token_create:

            '''
            检查过期的时间
            '''

            uptime = int(token_create.uptime.timestamp())

            result_time = self.check_token_time(uptime)

            print("result_time")
            print(self.token_con_time)
            print(result_time)

            if result_time - self.token_con_time > 0:

                #token过期返回刷新界面，重新登录

                return JsonResponse({"status":HTTP_401_UNAUTHORIZED,"result": {"token": ""}})

            self.update_token_time(token_create)



    def check_token_time(self,db_time):
        '''
        进行token的时间判断

        :param db_time:
        :return:
        '''

        now_time = time.time()

        result = now_time-db_time


        return int(result)

    @property
    def token_con_time(self):


        return  settings.TOKEN_CON_TIME


    def update_token_time(self,token):
        token.save()







