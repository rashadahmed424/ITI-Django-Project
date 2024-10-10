# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/password_change/', auth_views.PasswordChangeView.as_view(template_name='library/admin_password_change.html'), name='admin_password_change'),
    path('admin/password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='library/admin_password_change_done.html'), name='password_change_done'),
]
