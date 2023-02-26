from django import forms
from .models import Income, Purchase
from django.contrib.auth.models import User

class IncomeForm(forms.ModelForm):
    income_source = forms.CharField(label="Income Source")
    income_description = forms.CharField(label="Description")
    income = forms.FloatField(label="Income Received")
    
    class Meta:
        model = Income
        fields = ['income_source', 'income_description', 'income']
    

class PurchaseForm(forms.ModelForm):
    purchase_name = forms.CharField(label="Purchase Name")
    purchase_description = forms.CharField(label="Description")
    amount = forms.FloatField(label="Total Spent")
    
    class Meta:
        model = Purchase
        fields = ['purchase_name', 'purchase_description', 'amount']