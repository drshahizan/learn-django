from django import forms

from . import models


class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']

class RequestForm(forms.ModelForm):
    class Meta:
        model=models.EventRequest
        fields=['event_name','chairman_name','phone_no','email','venue','sdate','edate','description','attire','status']
