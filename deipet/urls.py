from django.contrib import admin
from django.urls import path
from .views import index, petlist

urlpatterns = [
    path('', index),
    path('list/', petlist),
]