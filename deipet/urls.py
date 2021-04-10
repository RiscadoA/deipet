from django.contrib import admin
from django.urls import path
from .views import index, add, pet, pets

urlpatterns = [
    path('', index),                            # Index page
    path('pets/<int:id>/', pet, name='pet'),    # Individual pet page
    path('pets/', pets, name='pets'),           # Pet list page
    path('add/', add, name='add'),              # Pet addition form page
]