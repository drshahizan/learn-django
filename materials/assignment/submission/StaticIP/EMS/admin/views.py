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
from customer import models as pmodels
from customer import forms as pforms

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'admin/index.html')

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer/customer-dashboard')
    else:
        return redirect('admin-dashboard')

@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict={
        'totalrequest':models.EventRequest.objects.all().count(),
        'totalapprovedrequest':models.EventRequest.objects.all().filter(status='Approved').count(),
        'totalrequestrejected':models.EventRequest.objects.all().filter(status='Rejected').count(),
        'totalrequestpending':models.EventRequest.objects.all().filter(status='Pending').count()
    }
    return render(request,'admin/admin_dashboard.html',context=dict)

@login_required(login_url='adminlogin')
def admin_customer_view(request):
    customers=pmodels.Customer.objects.all()
    return render(request,'admin/admin_customer.html',{'customers':customers})

@login_required(login_url='adminlogin')
def update_customer_view(request,pk):
    customer=pmodels.Customer.objects.get(id=pk)
    user=pmodels.User.objects.get(id=customer.user_id)
    userForm=pforms.CustomerUserForm(instance=user)
    customerForm=pforms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=pforms.CustomerUserForm(request.POST,instance=user)
        customerForm=pforms.CustomerForm(request.POST,request.FILES,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            return redirect('admin-customer')
    return render(request,'admin/update_customer.html',context=mydict)


@login_required(login_url='adminlogin')
def delete_customer_view(request,pk):
    customer=pmodels.Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return HttpResponseRedirect('/admin-customer')

@login_required(login_url='adminlogin')
def admin_request_view(request):
    requests=models.EventRequest.objects.all().filter(status='Pending')
    return render(request,'admin/admin_request.html',{'requests':requests})

@login_required(login_url='adminlogin')
def admin_request_history_view(request):
    requests=models.EventRequest.objects.all().exclude(status='Pending')
    return render(request,'admin/admin_request_history.html',{'requests':requests})

@login_required(login_url='adminlogin')
def update_approve_status_view(request,pk):
    req=models.EventRequest.objects.get(id=pk)
    req.status="Approved"
    req.save()
    requests=models.EventRequest.objects.all().filter(status='Pending')
    return render(request,'admin/admin_request.html',{'requests':requests})

@login_required(login_url='adminlogin')
def update_reject_status_view(request,pk):
    req=models.EventRequest.objects.get(id=pk)
    req.status="Rejected"
    req.save()
    return HttpResponseRedirect('/admin-request')