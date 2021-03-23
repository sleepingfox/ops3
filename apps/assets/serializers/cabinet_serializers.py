from rest_framework import viewsets
from rest_framework.decorators import action
from apps.assets.status_code.status import *

from apps.assets.serializers.serializers import *
from apps.assets.models import *

class CabinetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cabinet
        fields = "__all__"
