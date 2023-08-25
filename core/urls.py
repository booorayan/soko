from django.contrib.auth import views
from django.urls import path

from .views import *
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='index.html'), name='logout'),
]
