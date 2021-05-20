# threads/frontend/urls.py

from django.conf.urls import url
from django.urls import path

from .views import index_view

urlpatterns = [
    path('', index_view),
    url(r'^.*/$', index_view),
]