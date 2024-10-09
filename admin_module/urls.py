from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from admin_module.views import main,listbooks,bookdetails,bookdelete,bookedite,bookcreate,UpdatePass,custompassupdate,search_student

urlpatterns = [
    path('', main, name='admin_main'),  # Corrected name for better readability
    path('books/', listbooks.as_view(), name='books_index'),
    path('books/<int:pk>/', bookdetails.as_view(), name='book_details'),
    path('books/<int:pk>/delete/', bookdelete.as_view(), name='book_delete'),
    path('books/<int:pk>/edit/', bookedite.as_view(), name='book_edit'),
    path('books/create/', bookcreate.as_view(), name='book_create'),
    path('change-password/', UpdatePass.as_view(), name='change_password'),
    path('password-changed/', custompassupdate.as_view(), name='password_changed'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),  
    path('search/', search_student, name='search_student'),


]
