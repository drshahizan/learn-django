from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Shared Views
    path('', views.index, name='index'),
    path('register1/', views.StudentSignUpView.as_view(), name='register1'),
    path('login_form/', views.UserLoginView.as_view(), name='login_form'),
    path('login_user/', views.loginView, name='login_user'),
    path('logout_user/', views.logoutView, name='logout_user'),

    # Admin URLs
    path('dashboard_user/', views.dashboard_user, name='dashboard_user'),
    #path('course/', views.course, name='course'),
    path('isign/', views.InstructorSignUpView.as_view(), name='isign'),
    path('addlearner/', views.AdminLearner.as_view(), name='addlearner'),
    path('aluser/', views.ListUserView.as_view(), name='aluser'),
    path('aduser/<int:pk>', views.ADeleteuser.as_view(), name='aduser'),
    path('create_user_form/', views.create_user_form, name='create_user_form'),
    path('create_user/', views.create_user, name='create_user'),
    path('acreate_profile/', views.acreate_profile, name='acreate_profile'),
    path('auser_profile/', views.auser_profile, name='auser_profile'),


]
