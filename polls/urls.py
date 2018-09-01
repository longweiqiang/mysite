# -*- coding: UTF-8 -*-
# @Time       : 2018/8/22 22:45
# @Author     : Weiqiang.long
# @File       : urls.py.py
# @Software   : PyCharm
# @Description: 
# @TODO       :

from django.urls import path
from . import views

# 为 URL 名称添加命名空间
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]