from ops3.settings import INSTALLED_APPS
import importlib


def add_urls(urlpatterns):

    app_urls = [ x+".urls.urls"  for x in INSTALLED_APPS if "apps" in x]

    for i in app_urls:
        print(i)
        tmp = importlib.import_module(i)
        # urls.append(tmp.urlpatterns)
        urlpatterns+=tmp.urlpatterns

    print(urlpatterns)
    # return urls


