from django.db import models
from django.utils import timezone
from django.db.models.functions import Extract
from django.contrib.auth.models import User


class Purchase(models.Model):
    purchase_name = models.CharField(max_length=100)
    purchase_description = models.TextField()
    amount = models.FloatField()
    date_purchased = models.DateTimeField(default=timezone.now)
    # month_purchase = models.DateTimeField(default=timezone.now.month)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    

class Income(models.Model):
    income_recieved = models.FloatField()
    income_description = models.TextField()
    date_received = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    