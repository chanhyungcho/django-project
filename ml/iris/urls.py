from django.urls import re_path as url
from ml.iris import views
urlpatterns = [
    url(r'iris', views.iris)
]