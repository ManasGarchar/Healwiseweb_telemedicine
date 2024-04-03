# models.py
from django.db import models

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    p_name = models.CharField(blank=True, max_length=30)
    p_phone_no = models.IntegerField(default=0) 
    p_address = models.TextField(blank=True)
    dob = models.DateTimeField(blank=True, default=datetime.now)
    blood_group = models.CharField(max_length=5, blank=True)
    appoint_datetime = models.DateTimeField()
    disease_nm = models.CharField(blank=True,max_length=59)


    def __str__(self):
        return f"Appointment for {self.p_name} at {self.appoint_datetime}"




