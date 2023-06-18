from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.core.mail import send_mail

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            username = user.username
            message = f"Hello {username}!"
            if user.is_staff == 1:
                messages.success(request, message)
                return redirect('adminIndex')
            else:
                # Redirect to a success page.
                messages.success(request, message)
                return redirect('index')
        else:
            # Return an 'invalid login' error message.
            ...
            messages.success(request, "Wrong Username or Password!")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Sign Out Successful")
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # is_staff = form.cleaned_data['is_staff']
            # user = authenticate(username=username, password = password, is_staff = is_staff)
            # login(request, user)
            messages.success(request, "Sign Up Completed!")
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form':form,
    })