from django.conf.urls import url, include
from . import views

urlpatterns = [  
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^quote$', views.quote),
    url(r'^home$', views.home),
    url(r'^user/(?P<user_id>\d+)$', views.user)
]