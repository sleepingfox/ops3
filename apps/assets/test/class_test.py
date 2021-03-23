# class Grandfather:
#
#     name = "Grandfather"
#
#
#     def __init__(self,age=None,weight=None):
#
#         self.age = age
#         self.weight = weight
#
#
#     def whoami(self):
#         print("start grandfather's whoami")
#         print(self.name)
#
#
# class Father():
#     name = "Father"
#
#     def __init__(self, age=None, weight=None):
#         self.age = age
#         self.weight = weight
#
#     def whoami(self):
#         print("start father's whoami")
#         print(self.name)
#
#
# class Son(Grandfather,Father):
#     name = "Son"
#
#     def __init__(self, age=None, weight=None):
#         self.age = age
#         self.weight = weight
#
#     # def whoami(self):
#     #     print(self.name)
#     #
#
#     def test_update(self):
#
#         return self.whoami()
#
#     def test1(self):
#
#         print(self.__class__.__mro__)
#         return self.__class__.__mro__
#
#
#
# son = Son()
# father = Father()
# grandfather = Grandfather()
#
# son.whoami()


'''
上方为类的操作
'''

#
# name='C:/a/b/c/d.txt' #只想拿到顶级目录
# print(name.split('/',1))
#
#
# name='egon'
# print(name.center(30,'-'))
# print(name.ljust(30,'*'))
# print(name.rjust(30,'*'))
# print(name.zfill(50)) #用0填充

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import time

#
# def inner(func):
#
#     def timer(*args,**kwargs):
#         start = time.time()
#         res =func(*args,**kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return timer
#
#
# @inner
# def test(aaa):
#     time.sleep(1)
#     print("我是目标函数test")
#     print(aaa)
#     return "test"
#
# test(111)
#
# print(test(111))
# #test


#装饰有参数的函数
# import time
#
# def outter(outer):
#     def inner(func):
#         def timer(*args,**kwargs):
#             start = time.time()
#             res = func(*args,**kwargs)
#             stop = time.time()
#             print(stop-start)
#             print("带参数的装饰器",outer)
#             return 11111
#         return timer
#     print(outer)
#     return inner
#
# @outter("outer")
# def test(param_1):
#     time.sleep(1)
#     print("我是目标函数test")
#     print("我是参数%s" %param_1)
#
# #test = outter(test(xxx))
#
#
# a = test("param")
# print(a)


# x = range(10)
# print(x.__class__)
#
#
# name="zym"
# j=""
# for i in reversed(name):
#    j+=i
#
# print(j)
from apps.assets.test import aaa


import time
#
# print(time.time())
#
# print(time.localtime())
# print(time.gmtime())
#
print(time.strftime("%Y-%M-%d  %X"))

print(time.localtime())

print(time.mktime(time.localtime()))

print(time.strftime("%Y-%M-%d  %X", time.localtime()))


# shutil.copyfile("/root/test/test2","/root/test/test8")

import shutil
import os

print(os.getcwd())
# print(os.path.normpath(__file__))
path = os.getcwd()
print(path)


shutil.copyfile("%s/read" %path,"%s/test8" %path)







