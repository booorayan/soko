from django.urls import path

from .views import *

app_name = 'items'

urlpatterns = [
    path('new/', new, name='new'),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/delete/', delete, name='delete'),
]
