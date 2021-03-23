from rest_framework import serializers
from apps.assets import models

class IdcSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Idc
        fields = "__all__"
