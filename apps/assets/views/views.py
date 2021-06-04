from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.assets.status_code.status import *

from apps.assets.serializers.serializers import *
from apps.assets.models import *
from rest_framework.response import Response
# from .utils.myfilter import MyFilter
# class UserViewSet(viewsets.ModelViewSet):
# class UserViewSet(generics.GenericAPIView):
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from apps.assets.utils.pageUtil import pageUtil
from apps.assets.utils.sortByUtil import  sortByUtil
from apps.common.auth.myauth import myauth

from rest_framework_jwt.settings import api_settings




    # def list(self, request, *args, **kwargs):
    #     queryset =self.get_queryset()
    #     context = {'request': request}
    #
    #     serializer = UserSerializer(queryset,many=True,context=context)
    #     name2 =  {x.name: x.verbose_name for x in Asset._meta.fields}
    #     # print(serializer_class.__dict__)
    #     return response.Response(data={"data":serializer.data,"name2":name2},status="201")




## 主机查询

class AssetViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    serializer_class = AssetSerializer
    queryset = Asset.objects.all()

    # permission_classes = [IsAuthenticated]
    # authentication_classes = (JSONWebTokenAuthentication,)

    authentication_classes = [myauth]
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        print()
        print(request.query_params)
        print("token")
        queryset=Asset.objects.all()
        # key = request.query_params.keys()
        # print(key)
        # value = request.query_params[key]
        # print(value)

        print("-----------")
        if len(request.query_params)==1:
            for i in request.query_params:

                if i =="hostname":
                    queryset =   Asset.objects.filter(hostname__icontains=request.query_params[i])
                    print(queryset)
                    print(1111)

                elif i =="ip":
                    queryset =   Asset.objects.filter(ip__icontains=request.query_params[i])

                elif i =="asset_status":
                    queryset =   Asset.objects.filter(asset_status__icontains=request.query_params[i])

                elif i =="idc":
                    queryset =   Asset.objects.filter(idc__icontains=request.query_params[i])


        #分页
        currentPage = request.query_params.get("currentPage")
        pageSize = request.query_params.get("pageSize")



        # 排序，返回queryset
        sortBy = request.query_params.get("sortBy")
        order = request.query_params.get("order")

        print(queryset)
        print(222)

        fin_queryset = sortByUtil(sortBy, order,queryset).get_sort_order()

        serializer = AssetSerializer(fin_queryset, many=True)
        print(serializer.data)

        pageData = pageUtil(serializer.data,pageSize,currentPage,).pageData()

        pageTotal = len(serializer.data)

        return Response(data={"data": pageData,"pageTotal":pageTotal,"status":HTTP_200_OK})



    def retrieve(self, request, *args, **kwargs):

        obj = self.get_object()
        print("asset retrieve")

        res_data = self.get_serializer(obj)

        res_data2 = AssetDetailsSerializer(obj.assetdetails)
        print("res_data2")
        print(res_data2)

        # 重新整理数据
        # l1 = [i.verbose_name for i in obj._meta.fields]

        l2 = [i.verbose_name for i in obj.assetdetails._meta.fields]

        fin_data={}

        # for  i in enumerate(res_data.data.keys()):
        #     fin_data[l1[i[0]]]=res_data.data[i[1]]


        for  v in enumerate(res_data2.data.keys()):
            fin_data[l2[v[0]]]=res_data2.data[v[1]]

        return Response(data={"data":fin_data,"status":HTTP_200_OK,"msg":"成功"})





    def partial_update(self, request, *args, **kwargs):

        kwargs['partial']=True
        # serializers = self.get_serializer(data=request.data,partial=True)
        # print(kwargs.get("pk"))
        instance = self.get_object()
        # print(instance)
        print("partial")
        print(request.data)

        serializers = self.get_serializer(instance,data=request.data,partial=True)

        serializers.is_valid()
        print(serializers.errors)
        print("-----------")
        print(serializers.validated_data)

        serializers.save()

        return Response(data={"status":HTTP_201_CREATED,"msg":"成功创建"})


    def destroy(self, request, *args, **kwargs):


        obj = self.get_object()
        obj.delete()

        return Response(data={"status":HTTP_204_NO_CONTENT,"msg":'成功删除'})








##asset详细信息


class AssetDetailsViewSet(viewsets.ModelViewSet):

    serializer_class = AssetDetailsSerializer
    queryset = AssetDetails.objects.all()



    def list(self, request, *args, **kwargs):

        #  返回详细的信息
        obj = AssetDetails.objects.all()
        print(request.query_params)


        return Response("ok")


    def retrieve(self, request, *args, **kwargs):

        obj = self.get_object()
        res_data = self.get_serializer(obj)

        # 重新整理数据
        l1 = [i.verbose_name for i in obj._meta.fields]

        fin_data={}
        for  i in enumerate(res_data.data.keys()):
            fin_data[l1[i[0]]]=res_data.data[i[1]]

        return Response(data={"data":fin_data,"status":HTTP_200_OK,"msg":"成功"})


    # def list(self,request):
    #
    #
    #     #验证token操作
    #     # token =request._request.META.get('HTTP_AUTHORIZATION')
    #     # print("token")
    #     # obj = Token.objects.filter(key=token).first()
    #     # if not obj:
    #     #     return response.Response(data={"message":"登录已过期","status":HTTP_401_UNAUTHORIZED})
    #
    #
    #     query = Asset.objects.filter(pk=id)
    #
    #     if len(query)!=0:
    #         print("getServerDetails")
    #         data = query.first().assetdetails
    #         print(data)
    #         data.is_valid()
    #
    #         serializer = AssetDetailsSerializer(data)
    #         print(serializer.data)
    #     # return response.Response(obj)
    #         return Response(serializer.data)
    #
    #
    #     return Response({"status":HTTP_404_NOT_FOUND,"message":"找不到对应的id"})











# from rest_framework_jwt.settings import api_settings
#
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#
# payload = jwt_payload_handler(user)
# token = jwt_encode_handler(payload)


