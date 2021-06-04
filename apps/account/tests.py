# import datetime
#
# from django.test import TestCase
#
# # Create your tests here.
#
#
# #
# # def test1():
# #
# #     raise IOError
# #
# #
# # #
# # try:
# #     test1()
# #
# # except IOError as e :
# #     print(3 )
# #     print(e)
# #
# #
# #
# #
# # a = "null"
# #
#
# #
# #
# #
# # from django.contrib.sessions.middleware import SessionMiddleware
# #
# #
# # from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# #
# #
# # from rest_framework_jwt.utils  import jwt_decode_handler
#
#
#
#
#
#
#
#
#
#
#
#
# from Crypto import Random
# from Crypto.Hash import SHA
# from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
# from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
# from Crypto.PublicKey import RSA
# import base64
#
# from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
#
#
#
# # ---test数据---
# JWT_PAYLOAD={
#     # 过期时间
#     'exp': datetime.datetime.utcnow()+datetime.timedelta(seconds=3),
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
#     "iat": datetime.datetime.utcnow(),
#
#     "data":{
#         "userid":"",
#
#     }
# }
# # ------
#
# import jwt
# import  cryptography
#
#
#
#
# public_key = """-----BEGIN PUBLIC KEY-----
# MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQChjX25bfIRqOGCYp8FJ/Qqu/3b
# ptN++hcU1Msb+8T7pmdE3N7mcLDdN3ZtiOAMvwn9Ml7ZH94YIb4javLi6FCLwfrD
# DSzmAI6uAXLjrNBecMJ99iz+OG1+DX6MlIj3ddzrJEv1/3Xok545gtieSeTKypbU
# TtXWcK+btCmdmwMjIwIDAQAB
# -----END PUBLIC KEY-----"""
#
#
# private_key = """
# -----BEGIN RSA PRIVATE KEY-----
# MIICXQIBAAKBgQChjX25bfIRqOGCYp8FJ/Qqu/3bptN++hcU1Msb+8T7pmdE3N7m
# cLDdN3ZtiOAMvwn9Ml7ZH94YIb4javLi6FCLwfrDDSzmAI6uAXLjrNBecMJ99iz+
# OG1+DX6MlIj3ddzrJEv1/3Xok545gtieSeTKypbUTtXWcK+btCmdmwMjIwIDAQAB
# AoGAMhPlBATTw6ug88TUXEnNQy3w/BSTfMnTO87Wgv8hSYyEeHEq2y3VdU1K9Zs3
# MFxLoWPqyM07ECntgZcWYUX4KUxMM+8nN6/miegabwGrePNcavmnxOtnmGHoGtox
# z+4y+zgJUxvQWaubjGdCZZRvyKGxEEapYNbtYStRzH+EB0kCQQDKNpONRkQP+9JO
# 1JqhrCnBIp/FdM0Cc2LLtJRNOdRs1zP6BnRXVaFHPX0VhKu+HvY0H9UiT8BaauJa
# 0Z3a/7InAkEAzIYyGohGPKipSJWzyiytxrSxqw7vE2rHhrAdUsFrJBqnabnXiM42
# Fc99n5xLeiBFTWrpjZw7wv6rwXh2fYIwpQJBAK2moJ+5r8lqH/jCauhbyJ+q9DnF
# TCjGnhkBQjnvZ5TwWhpkYJR/XLio/Tn1bOcf/55Tl9yXUEBVeX00dbMT0hECQCXr
# j6iZsaQXhWN+1hnbFNEtuW9E0pDgEGRpjNZGJE5KXtXcbhjgWujKUrlgKiJXj2He
# O7VUzUPHIiM56YY1uD0CQQCYgcXmi609VUnHl+uaPjHzi4KhD7+4kkeaWIADAKIG
# Tv9R0VasmNCiIxvUOTNgc4gxdzkLXwcDN++bS3qi3Wj7
# -----END RSA PRIVATE KEY-----
# """
#
# print("start iat")
# print(JWT_PAYLOAD['iat'])
#
# # jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))
#
# # encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256")
#
#
# encoded = jwt.encode(JWT_PAYLOAD, private_key, algorithm="RS256")
# import time
#
# print(encoded)
# print(JWT_PAYLOAD["exp"])
# print(JWT_PAYLOAD["iat"])
#
# print("JWT_PAYLOAD")
# print(JWT_PAYLOAD)
#
# print("111111")
# print(time.time())
#
# print("222222")
# print(datetime.datetime.now())
#
# time.sleep(4)
#
# # print("3333")
# # print(datetime.datetime.now())
# # print(datetime.datetime.now()+datetime.timedelta(seconds=5))
# # print("444444444")
# # print(time.time())
# # time.sleep(2)
# # print(time.time())
#
# # print(time.time()+datetime.timedelta(seconds=1))
#
# decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
#
#
#
# print(decoded)

import test2

from ops3 import settings

a = "JWT_REFRESH_PAYLOAD"
obj = getattr(settings,a)

print(obj)
