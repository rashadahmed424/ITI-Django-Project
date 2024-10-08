from django.urls import path
from students.views import liststudents
urlpatterns = [

path('',liststudents.as_view(),name='students.index')

]