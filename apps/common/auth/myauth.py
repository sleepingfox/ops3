import datetime

import jwt
from django.http import JsonResponse
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from ops3 import settings

from apps.common.tokenUtils import TokenUtils

from jwt.exceptions import ExpiredSignature
from jwt.exceptions import DecodeError

# ---test数据---
# JWT_PAYLOAD={
#     # 过期时间
#     'exp': datetime.datetime.now()+datetime.timedelta(seconds=1),
#     #datetime.datetime(2021, 6, 1, 10, 11, 15, 106515) +1days
#
#     #token的生效时间
#     #fbf
#
#     # token的签发者
#     "iss": 'zhouyiming',
#
#     #接收者
#     #aud
#
#     #token开始的时间
#     "iat": datetime.datetime.now(),
#
#     "data":{
#         "userid":"",
#
#     }
# }
# ------

class myauth(BaseAuthentication):


    def  authenticate(self, request):

        """
        认证token
        :param request:
        :return:
        """


        # 获取token

        print("myauth")
        # print(request.META.HTTP_ACCESS_TOKEN)
        print(request.META)
        print("_________")
        token = request.META.get("HTTP_AUTHORIZATION")
        print(token)

        res = ""


        # secret_key =  settings.JWT_SECRET_PUBLIC_KEY.encode("utf-8")
        secret_key =  settings.JWT_SECRET_PUBLIC_KEY

        print(secret_key)
        print("========")
        print("now time")
        print(datetime.datetime.utcnow())

        # print(jwt.decode(token,secret_key, algorithms=["RS256"]))


        # test
        # token ="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MjI3MTQxOTAsImlzcyI6Inpob3V5aW1pbmciLCJpYXQiOjE2MjI3MTQxODgsImRhdGEiOnsidXNlcmlkIjoiIiwidXNlciI6MX19.mutKKL8GjJX7_BPalF3suRLocEO38BRUYJW9z4M_Xhz_1iRO7wEwkU8_nTQmP58X-GKFVF5r6xWtAbWXQq7NV-pr5SbgS9ZateSLUT7fXJop6zusWc8Yy0P72nB3dj7VMRSFIifnthCiQ8YZJonudVuJqxAfrecxS_dWnSytUFE"

        try:
            res = jwt.decode(token,secret_key, algorithms=["RS256"])
            # decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
            print(res)
            print("res")

        except ValueError:

            msg = "key值错误"
            print(msg)
            raise AuthenticationFailed({"data": "", "status": 401, "msg": msg})



        except DecodeError:

            msg = "Invalid token type"


            print(msg)
            raise AuthenticationFailed({"data": "", "status": 401, "msg": msg})

        except ExpiredSignature:

            msg = "token已过期"
            # 重新刷新一个token



            print(msg)
            raise AuthenticationFailed({"data": "", "status": 401, "msg": msg})




        #
        # except Exception as e :
        #
        #     print("^^^^^^^^^^^^^^^^")
        #     print(e)
        #     raise AuthenticationFailed({"data": "", "status": 200, "msg": e})



        # 增加token的持续时间

        TokenUtils().update_access_token_exp()

        print(settings.JWT_PAYLOAD["exp"])

        return (res,token)




    def authenticate_header(self, request):


        # print("auth_header")

        return JsonResponse({"data": "", "status": 401, "msg": "token非法"})





