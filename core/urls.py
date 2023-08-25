from django.contrib.auth import views
from django.urls import path

from .views import *
from .forms import LoginForm, PasswordResetForm

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('password-reset/', views.PasswordResetView.as_view(template_name='password_reset.html'), name='password-reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password-reset-confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password-reset-complete'),
]
