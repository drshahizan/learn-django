from django.db import models
from customer import models as cmodels

class EventRequest(models.Model):
    request_by_customer=models.ForeignKey(cmodels.Customer,null=True,on_delete=models.CASCADE)
    event_name=models.CharField(max_length=100)
    chairman_name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    attiregroup=models.CharField(max_length=10)
    description=models.CharField(max_length=500)
    status=models.CharField(max_length=20,default="Pending")
    sdate=models.DateField(auto_now=True)
    edate=models.DateField(auto_now=True)
    def __str__(self):
        return self.attiregroup

        