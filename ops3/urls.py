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
from django.contrib import admin
from django.urls import path,include

from rest_framework.documentation import include_docs_urls


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",

      contact=openapi.Contact(email="zhouyiming5824@163.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




urlpatterns = [
    # path(r'login/', include('rest_framework.urls',namespace="rest_framework")),
    # path('admin/', admin.site.urls),

    path('assets/', include('apps.assets.urls.urls')),
    path("account/",include('apps.account.urls')),


    # path('assets/', include('apps.assets.urls.urls',namespace='api-assets')),
    # path('apps/', include('apps.assets.urls.urls', namespace='api-assets')),
    # path('apps/',include('apps.user.urls.urls',namespace ="api-user"))

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('get_token/', obtain_jwt_token),

    path('refresh_token/' ,refresh_jwt_token)





]


# from apps.common.urls_collect import urls_collect
#
#
# urls_collect.add_urls(urlpatterns)


