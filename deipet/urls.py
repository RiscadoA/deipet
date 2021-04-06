from django.contrib import admin
from django.urls import path
from .views import index, pet, pets

urlpatterns = [
    path('', index),
    path('pets/<int:id>/', pet, name='pet'),
    path('pets/', pets, name='pets'),
]