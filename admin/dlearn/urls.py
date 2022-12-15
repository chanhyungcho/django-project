from django.urls import re_path as url

from admin.dlearn import fashion_view

urlpatterns = [
    url(r'fashion', fashion_view.fashion)
]