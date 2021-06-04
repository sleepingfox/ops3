import jwt
import rest_framework
from django.http import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin

from rest_framework.authtoken.models import Token
from rest_framework import authtoken
import time

from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework_jwt.views import VerifyJSONWebToken, RefreshJSONWebToken

from ..status_code.status import *
from ops3 import settings

class InterceptorMiddleware(MiddlewareMixin):


    def   process_request(self,request):

        print("token_control")



        token = request.META.get("HTTP_AUTHORIZATION")


        # if token=="null":
        #
        #     print("pass")
        #     return JsonResponse({"status": HTTP_401_UNAUTHORIZED, "result": {"token": ""}})

        # if token!="null" and token!=None:
        if token and token!="null":

            print(token)
            dic ={}
            dic["token"] = token
            if_login = request.META.get("PATH_INFO")


            print("status")

            from rest_framework.exceptions import ValidationError

            try :

                status = VerifyJSONWebTokenSerializer().validate(dic)

                print(status)

                if status.get("user"):
                    # 如果token验证成功
                    status["user"] = status["user"].username
                    print("fin_status")
                    print(status)

            except (Exception,ValidationError)  as e:

                print(e)
                print("try catch")
                return JsonResponse({"data": "", "status": 401, "msg": "token非法"})




            # if status.get("user"):
            #     # 如果token验证成功
            #     status["user"] = status["user"].username
            #     print("fin_status")
            #     print(status)
            #     # return JsonResponse({"data":status,"status":200,"msg":"成功"})



            # else:
            #
            #     return JsonResponse({"data":"","status":"401","msg":"token非法"})




            # user = VerifyJSONWebTokenSerializer().validate(dic).get("user")
            #
            # if user:
            #
            #     return JsonResponse({"status":HTTP_401_UNAUTHORIZED,"data": {"token": ""},"msg":"token錯誤"})
            #
            #
            # print("111")
            # print(user)


            # raise AuthenticationFailed('认证失败')




        # if request.META.get("PATH_INFO") =="/account/login/":
        #     login路径不验证token





        # RefreshJSONWebToken().post(request={"username": "zym", "password": "123", "token": "1111111111111111111111"})

        # return JsonResponse({"status": HTTP_401_UNAUTHORIZED, "result": {"token": ""}})



    #     token_create = Token.objects.filter(key=token).first()
    #
    #     if not token_create and if_login != "/users/login/":
    #
    #         return JsonResponse({"status":HTTP_401_UNAUTHORIZED,"result": {"token": ""}})
    #
    #
    #
    #     if token_create:
    #
    #         '''
    #         检查过期的时间
    #         '''
    #
    #         uptime = int(token_create.uptime.timestamp())
    #
    #         result_time = self.check_token_time(uptime)
    #
    #         print("result_time")
    #         print(self.token_con_time)
    #         print(result_time)
    #
    #         if result_time - self.token_con_time > 0:
    #
    #             #token过期返回刷新界面，重新登录
    #
    #             return JsonResponse({"status":HTTP_401_UNAUTHORIZED,"result": {"token": ""}})
    #
    #         self.update_token_time(token_create)
    #
    #
    #
    # def check_token_time(self,db_time):
    #     '''
    #     进行token的时间判断
    #
    #     :param db_time:
    #     :return:
    #     '''
    #
    #     now_time = time.time()
    #
    #     result = now_time-db_time
    #
    #
    #     return int(result)
    #
    # @property
    # def token_con_time(self):
    #
    #
    #     return  settings.TOKEN_CON_TIME
    #
    #
    # def update_token_time(self,token):
    #     token.save()







