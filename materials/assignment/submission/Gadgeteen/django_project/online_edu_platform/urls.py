from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register1/', views.StudentSignUpView.as_view(), name='register1'),
    
]
