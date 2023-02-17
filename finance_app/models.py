from django.db import models
from django.utils import timezone
from django.db.models.functions import Extract
from django.contrib.auth.models import User
import datetime


class Purchase(models.Model):
    purchase_name = models.CharField(max_length=100)
    purchase_description = models.TextField()
    amount = models.FloatField()
    date_purchased = models.DateTimeField(default=datetime.datetime.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    

class Income(models.Model):
    income_source = models.TextField()
    income_description = models.TextField()
    amount = models.FloatField()
    date_received = models.DateTimeField(default=datetime.datetime.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    