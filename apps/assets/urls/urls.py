"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.viecmdbws import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers

from apps.assets.views.cabinet_views import CabinetViewSet
from apps.assets.views.idc_views import IdcViewSet
from apps.assets.views.views import *
from django.urls import path




# router.register(r'api/0.0.0/user', UserViewSet,'user')


# from django.urls import path, include
from apps.assets.views import views

app_name = "assets"

router = routers.DefaultRouter()
router.register(r'assets', AssetViewSet, 'assets')
router.register(r'idcs', IdcViewSet, 'idc')
router.register(r'cabinets', CabinetViewSet, 'cabinet')
router_urls=router.urls
print("router_urls")
print(router_urls)




urlpatterns = [
    path('assets/assetsdetails/<int:id>/', views.AssetViewSet.as_view({"get":'list_details'}), name='assetsdetails'),
]

urlpatterns += router.urls
# urlpatterns = [
#     # url('^servers/',views.Host.as_view(),name="host" ),
#     # url(r'assets/host/(?P<host>.+/$)', include('assets.urls')),
#
# ]

