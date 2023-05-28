from django.contrib import admin

# Register your models here.
from .models import BlogModel, Profile

admin.site.register(BlogModel)
admin.site.register(Profile)
