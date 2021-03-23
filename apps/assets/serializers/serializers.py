from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.assets import models
from apps.assets.models import AssetDetails, Idc,Cabinet,UserInfo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'password',"login_method"]
        fields = "__all__"






class DisplayChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        """返回选项的值"""
        return self._choices[obj]







class AssetSerializer(serializers.ModelSerializer):


    ASSET_STATUS = [
        (str(1), u"使用中"),
        (str(2), u"未使用"),
        (str(3), u"故障"),
        (str(4), u"其它"),
    ]

    ASSET_TYPE = [
        (str(1), u"物理机"),
        (str(2), u"虚拟机"),
        (str(3), u"容器"),
        (str(4), u"网络设备"),
        (str(5), u"安全设备"),
        (str(6), u"其他")
    ]

    idc = serializers.CharField(source='idc.name')
    cabinet = serializers.CharField(source='cabinet.name')
    account = serializers.CharField(source="account.username")

    def create(self, validated_data):
        print(validated_data)
        print(validated_data.__dict__)
        print("mycreate")


    class Meta:
        model = models.Asset
        fields="__all__"
        # exclude = ['asset_type']
        read_only_fields =["id"]
        # depth = 0


    def update(self, instance, validated_data):

        print(validated_data)
        print(instance)
        print("serlializes update")



        instance.idc = Idc.objects.filter(name=validated_data["idc"]['name']).first()
        instance.cabinet = Cabinet.objects.filter(name=validated_data["cabinet"]['name']).first()
        instance.account = UserInfo.objects.filter(username=validated_data["account"]['username']).first()

        # serializer = self(instance, data=validated_data.data)
        #
        # serializer.save()


        # instance.cabinet = validated_data["cabinet"]['name']
        # instance.account = validated_data["account"]['name']


        # instance.save()
        # return instance
        return instance


class AssetDetailsSerializer(serializers.ModelSerializer):

    # asset = serializers.CharField(source='Asset.Assetname')
    # "idc": 1,
    # "Cabinet": 1
    class Meta:
        model = AssetDetails
        fields = '__all__'

'''
#超链接的形式
'''


