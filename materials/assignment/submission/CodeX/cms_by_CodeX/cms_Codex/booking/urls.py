from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminIndex', views.adminIndex, name='adminIndex'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
    path('user-delete/<int:id>', views.userDelete, name='userDelete'),
    path('service', views.service, name='service'),
    path('adminPanel', views.adminPanel, name='adminPanel'),
    path('bookingList', views.bookingList, name='bookingList'),
    path('adminUpdate/<int:id>', views.adminUpdate, name='adminUpdate'),
    
]