from apps.user.views import views

from rest_framework  import routers
from django.urls import path

from ..views import views

router = routers.DefaultRouter()
router.register("user",views.UserView,"user")

router_urls=router.urls
print("router_urls")
print(router_urls)


app_name = "user"

urlpatterns = [
    path('login/', views.AuthUserView.as_view({'post': 'login'})),


]

urlpatterns+= router.urls
