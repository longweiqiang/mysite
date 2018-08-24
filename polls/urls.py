# -*- coding: UTF-8 -*-
# @Time       : 2018/8/22 22:45
# @Author     : Weiqiang.long
# @File       : urls.py.py
# @Software   : PyCharm
# @Description: 
# @TODO       :

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
]