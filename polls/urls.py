#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 11:02
# @Author  : yc
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from . import  views

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),  # name 被模板以{% url ‘detail’ %}调用
    # url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),

# 改进
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),   # as_view()  需要写调用
    url(r'^(?P<pk>[0-9]+)/results/$',views.ResultView.as_view(),name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]