from rest_framework import viewsets, mixins
from rest_framework.decorators import action
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


class UserViewSet(viewsets.GenericViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def retrieve(self,request):
    #     print(request)
    #     print('retrieve')
    #
    #     return {"ok"}

    def list(self,request):

        query_set = self.get_queryset()

        serializer = UserSerializer(query_set,many=True)
        return Response(serializer.data)


    # @action(methods=['post'],detail=False)
    # def login(self,request):
    #     print("zzzzzzzzzzzzzzzzzzz")
    #     info_dic = request.data
    #     username= info_dic.get("username")
    #     print(username)
    #     print(info_dic)
    #     # obj = User.objects.filter(username=username).first()
    #
    #     print("obj")
    #     print(info_dic["password"])
    #     # print(obj.password)
    #     # print(info_dic[username])
    #     user =authenticate(username=username,password=info_dic["password"])
    #     if user:
    #
    #         print(user.id)
    #         #更新操作，登陆一次生成一个token
    #         Token.objects.filter(user_id=user.id).delete()
    #         token = Token.objects.create(user=user)
    #
    #         #判断密码是否正确
    #         return response.Response(data={"message": "登录成功", "status": HTTP_200_OK, "result": {"token":token.key,"user":{"username":user.username}}})
    #
    #     return response.Response(data={"message": "登陆失败", "status": HTTP_404_NOT_FOUND, "result": {}})



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



    @action(methods=['get'],detail=False,url_path="assetsdetails")
    def list_details(self,request,id):


        #验证token操作
        # token =request._request.META.get('HTTP_AUTHORIZATION')
        # print("token")
        # obj = Token.objects.filter(key=token).first()
        # if not obj:
        #     return response.Response(data={"message":"登录已过期","status":HTTP_401_UNAUTHORIZED})


        query = Asset.objects.filter(pk=id)

        if len(query)!=0:
            print("getServerDetails")
            data = query.first().assetdetails
            print(data)
            data.is_valid()

            serializer = AssetDetailsSerializer(data)
            print(serializer.data)
        # return response.Response(obj)
            return Response(serializer.data)


        return Response({"status":HTTP_404_NOT_FOUND,"message":"找不到对应的id"})





    def partial_update(self, request, *args, **kwargs):

        kwargs['partial']=True




        return self.update(request, *args, **kwargs)

        # instance = self.update(request,*args,**kwargs)

        # serializer =  self.get_serializer(instance, data=self.request.data)
        # serializer.

        # print(instance)

        # serializer = self.get_serializer(instance, data=request.data,)
        # serializer.is_valid(raise_exception=True)
        #
        # print(serializer.is_vaild())
        # serializer.save()
        # return self.update(request,*args,**kwargs)
        # self.get_serializer(self.update(request,*args,**kwargs),data = self.request.data).save()


        return Response("ok")


    # def update(self, request, pk):
    #
    #     print("进行更新操作")
    #     print("pk")
    #     print(pk)
    #     print("request.data")
    #     print(request.data)
    #
    #     old_obj_test = Asset.objects.filter(pk=pk).first()
    #
    #     test1 = AssetSerializer(data=request.data)
    #     test1.is_valid()
    #     if "unique" in  test1.errors.get("Assetname"):
    #         print("进行更新")
    #
    #
    #
    #     # old_obj = AssetSerializer(Asset.objects.filter(pk=pk).first()).data
    #     # old_obj = AssetSerializer(Asset.objects.filter(pk=pk).first(),data=request.data,partial=True)
    #     # print("old_data")
    #     # print(old_obj)
    #
    #
    #     # print(old_obj.is_valid())
    #     # old_obj.is_valid()
    #     # old_obj.save()
    #
    #     # if request.data == old_obj:
    #     #     print("无需更改")
    #     #     return response.Response(data={"msg": "更改成功","status":HTTP_200_OK})
    #     #
    #     # Asset.objects.filter(pk=pk).update(**request.data)
    #
    #
    #     print("===========post")
    #
    #
    #
    #     return Response(data={"msg": "更改成功", "status": HTTP_200_OK})














