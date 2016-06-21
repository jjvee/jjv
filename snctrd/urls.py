#-*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import url
from . import views


app_name = 'snctrd'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^$', views.index, name = 'home'),
    url(r'^meetings/(?P<meeting_id>.+)/$', views.meetings),
    url(r'^order/(?P<meeting_id>.+)/$', views.order),
    url(r'^createOrder/$', views.createOrder),
    url(r'^deleteOrder/$', views.deleteOrder),
    url(r'^orderSummary/(?P<meeting_id>.+)/$', views.orderSummary),
]