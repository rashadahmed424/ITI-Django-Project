from django.contrib import admin
from django.urls import path
from admin_module.views import main,listbooks,bookdetails,bookdelete,bookedite,bookcreate

urlpatterns = [
    path('',main,name='admin.main'),
    path('books',listbooks.as_view(),name='books.index'),
    path('bdetails/<int:pk>',bookdetails.as_view(),name='book_details'),
    path('bdel/<int:pk>/',bookdelete.as_view(),name='book_delete'),
    path('bedite/<int:pk>/',bookedite.as_view(),name='book_edite'),
    path('bcreate',bookcreate.as_view(),name='book_create'),


]
