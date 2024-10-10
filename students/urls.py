from django.urls import path
from students.views import liststudents, signup_view

urlpatterns = [

    path('', liststudents.as_view(), name='students.index'),
    path('signup/', signup_view, name='signup'),
]
