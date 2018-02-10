'''
Created on 2018年2月10日

@author: Carol
'''
from django.urls import path

from . import views

urlpatterns = [
    path(r'index/' , views.index),
    ]