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



urlpatterns = [
    # url(r'login/', include('rest_framework.urls',namespace="rest_framework")),
    path('admin/', admin.site.urls),
    # url(r'^assets/', include('apps.assets.urls')),
    # path('assets/', include('apps.assets.urls.urls',namespace='api-assets')),
    # path('apps/', include('apps.assets.urls.urls', namespace='api-assets')),
    # path('apps/',include('apps.user.urls.urls',namespace ="api-user"))
]


from apps.common.urls_collect import urls_collect


urls_collect.add_urls(urlpatterns)


