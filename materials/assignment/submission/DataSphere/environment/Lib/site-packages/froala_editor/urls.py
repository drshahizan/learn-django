from django.urls import path, re_path
from froala_editor import views

urlpatterns = [
    path('image_upload/', views.image_upload, name='froala_editor_image_upload'),
    path('file_upload/', views.file_upload, name='froala_editor_file_upload'),
]
