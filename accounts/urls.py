from django import urls
from django.urls import path,include
# from admin_module.views import profile
from accounts.views import profile
urlpatterns=[
    path('',include("django.contrib.auth.urls")),
    path('profile/',profile,name='profile')
]