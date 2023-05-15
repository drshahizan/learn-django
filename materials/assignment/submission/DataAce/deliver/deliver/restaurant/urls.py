from django.urls import path
from .views import Dashboard, OrderDetails


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>/', OrderDetails.as_view(), name= 'order-details'),
]