from django.urls import re_path as url
from shop.s_users import views
urlpatterns = [
    url(r'iris', views.iris)
]