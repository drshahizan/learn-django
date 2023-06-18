from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum,Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User
from admin import forms as bforms
from admin import models as bmodels


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.attiregroup=customerForm.cleaned_data['attiregroup']
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request,'customer/customersignup.html',context=mydict)

def customer_dashboard_view(request):
    customer= models.Customer.objects.get(user_id=request.user.id)
    dict={
        'requestpending': bmodels.EventRequest.objects.all().filter(request_by_customer=customer).filter(status='Pending').count(),
        'requestapproved': bmodels.EventRequest.objects.all().filter(request_by_customer=customer).filter(status='Approved').count(),
        'requestmade': bmodels.EventRequest.objects.all().filter(request_by_customer=customer).count(),
        'requestrejected': bmodels.EventRequest.objects.all().filter(request_by_customer=customer).filter(status='Rejected').count(),

    }
   
    return render(request,'customer/customer_dashboard.html',context=dict)

def make_request_view(request):
    request_form=bforms.RequestForm()
    if request.method=='POST':
        request_form=bforms.RequestForm(request.POST)
        if request_form.is_valid():
            event_request=request_form.save(commit=False)
            event_request.attiregroup=request_form.cleaned_data['attiregroup']
            customer= models.Customer.objects.get(user_id=request.user.id)
            event_request.request_by_customer=customer
            event_request.save()
            return HttpResponseRedirect('my-request')  
    return render(request,'customer/makerequest.html',{'request_form':request_form})

def my_request_view(request):
    customer= models.Customer.objects.get(user_id=request.user.id)
    event_request=bmodels.EventRequest.objects.all().filter(request_by_customer=customer)
    return render(request,'customer/my_request.html',{'event_request':event_request})
