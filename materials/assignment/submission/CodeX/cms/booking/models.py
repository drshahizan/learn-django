from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Oil Change and Oil Filter", "Oil Change and Oil Filter"),
    ("Windshield wipers and fluid", "Windshield wipers and fluid"),
    ("Air and cabin filter replacement", "Air and cabin filter replacement"),
    ("Tire replacement and wheel balance and rotation", "Tire replacement and wheel balance and rotation"),
    ("Battery replacement","Battery replacement"),
    ("Brake Repair","Brake Repair"),
    ("Coolant system services","Coolant system services"),
    )
TIME_CHOICES = (
    ("10 AM","10 AM"),
    ("10:30 AM","10:30 AM"),
    ("11 AM","11 AM"),
    ("11:30 AM","11:30 AM"),
    ("12 PM","12 PM"),
    ("12:30 PM","12:30 PM"),
    ("1 PM","1 PM"),
    ("1:30 PM","1:30 PM"),
    ("2 PM","2 PM"),
    ("2:30 PM","2:30 PM"),
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Oil Change and Oil Filter")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="10 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"