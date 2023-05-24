from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('customerlogin', LoginView.as_view(template_name='customer/customerlogin.html'),name='customerlogin'),
    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('make-request', views.make_request_view,name='make-request'),
    path('my-request', views.my_request_view,name='my-request'),
]