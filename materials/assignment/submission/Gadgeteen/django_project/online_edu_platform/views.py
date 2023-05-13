from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.core import serializers
from django.conf import settings
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from datetime import datetime, date
from django.core.exceptions import ValidationError
from . import models
import operator
import itertools
from django.db.models import Avg, Count, Sum
from django.forms import inlineformset_factory
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from online_edu_platform.models import (Student, Course, User,Profile,Instructor)

# Create your views here.
def index(request):
    # Page from the theme 
    return render(request, 'index.html')

#Register Form
class StudentSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label=("Confirm Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    )
    class Meta(UserCreationForm.Meta):

        model = User
        fields = ('username', 'email', )
        widgets = {
        'username': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }),
        'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@company.com'
        })
        }

    def __init__(self, *args, **kwargs):
            super(StudentSignUpForm, self).__init__(*args, **kwargs)

            for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None    

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user
    
#Register View
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'sign-up.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

#Login Form    
class LoginForm(AuthenticationForm):
  username = UsernameField(label=("Your Username"), widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
  password = forms.CharField(
      label=("Your Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
  )

#Login_form View
class UserLoginView(LoginView):
  form_class = LoginForm
  template_name = 'sign-in.html'

#Logout View
def logoutView(request):
	logout(request)
	return redirect('index')

#Login View
def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if user.is_admin or user.is_superuser:
				return redirect('dashboard')
			elif user.is_instructor:
			    return redirect('instructor')
			elif user.is_student:
			    return redirect('student')
			else:
			    return redirect('login_form')
		else:
		    messages.info(request, "Invalid Username or Password")
		    return redirect('login_form')
                
# Admin Views
def dashboard_user(request):
    student = User.objects.filter(is_student=True).count()
    instructor = User.objects.filter(is_instructor=True).count()
    course = Course.objects.all().count()
    users = User.objects.all().count()
    context = {'student':student, 'course':course, 'instructor':instructor, 'users':users}

    return render(request, 'dashboard/admin/dashboard.html', context)

class InstructorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
            super(InstructorSignUpForm, self).__init__(*args, **kwargs)

            for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None

class InstructorSignUpView(CreateView):
    model = User
    form_class = InstructorSignUpForm
    template_name = 'dashboard/admin/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'instructor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Instructor Was Added Successfully')
        return redirect('isign')


class AdminLearner(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'dashboard/admin/learner_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'learner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Student Was Added Successfully')
        return redirect('addlearner')



def course(request):
	if request.method == 'POST':
		name = request.POST['name']
		color = request.POST['color']

		a = Course(name=name, color=color)
		a.save()
		messages.success(request, 'New Course Was Registed Successfully')
		return redirect('course')
	else:
	     return render(request, 'dashboard/admin/course.html')	

#111
class ListUserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/admin/list_users.html'
    context_object_name = 'users'
    paginated_by = 10

    def get_queryset(self):
        return User.objects.order_by('-id')



class ADeleteuser(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'dashboard/admin/confirm_delete2.html'
    success_url = reverse_lazy('aluser')
    success_message = "User Was Deleted Successfully"



def create_user_form(request):
    return render(request, 'dashboard/admin/add_user.html')


def create_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)

        a = User(first_name=first_name, last_name=last_name, username=username, password=password, email=email, is_admin=True)
        a.save()
        messages.success(request, 'Admin Was Created Successfully')
        return redirect('aluser')
    else:
        messages.error(request, 'Admin Was Not Created Successfully')
        return redirect('create_user_form')



def acreate_profile(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birth_date = request.POST['birth_date']
        bio = request.POST['bio']
        phonenumber = request.POST['phonenumber']
        city = request.POST['city']
        country = request.POST['country']
        avatar = request.FILES['avatar']
        hobby = request.POST['hobby']
        current_user = request.user
        user_id = current_user.id
        print(user_id)

        Profile.objects.filter(id = user_id).create(user_id=user_id,phonenumber=phonenumber, first_name=first_name, last_name=last_name, bio=bio, birth_date=birth_date, avatar=avatar, city=city, country=country)
        messages.success(request, 'Your Profile Was Created Successfully')
        return redirect('auser_profile')
    else:
        current_user = request.user
        user_id = current_user.id
        users = Profile.objects.filter(user_id = user_id)
        users = {'users': users}
        return render(request, 'dashboard/admin/create_profile.html', users)     



def auser_profile(request):
    current_user = request.user
    user_id = current_user.id
    users = Profile.objects.filter(user_id = user_id)
    users = {'users': users}
    return render(request, 'dashboard/admin/user_profile.html', users)
