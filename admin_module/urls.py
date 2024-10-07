from django.contrib import admin
from django.urls import path
from admin_module.views import main

urlpatterns = [
    path('',main,name='admin.main')
]
