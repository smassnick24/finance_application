from django.shortcuts import render
from django.utils import timezone
import datetime

# creating dummy data to push to templates for testing

purchase_list = [
    {
        'purchase_name': "Gasoline",
        'purchase_description': "Gas for school",
        'amount': 40.00,
        'date_purchased': str(datetime.datetime.now()),
        'owner': "smassnick24"
    },
    {
        'purchase_name': "Snacks",
        'purchase_description': "Snacks for aubrey",
        'amount': 20.17,
        'date_purchased': str(datetime.datetime.now()),
        'owner': "smassnick24"
    },
]

income_list = [
    {
        "income_source": "Wesco",
        "income_description": "paycheck from wesco",
        "amount": 200.13,
        "date_received": str(datetime.datetime.now()),
        "owner": "smassnick24"
    },
    {
        "income_source": "Wesco",
        "income_description": "paycheck from wesco",
        "amount": 313.13,
        "date_received": str(datetime.datetime.now()),
        "owner": "smassnick24"
    }
]

def purchase_page(request):
    context = {
        'purchases': purchase_list
    }
    return render(request, "finance_app/purchases.html", context)

def income_page(request):
    context = {
        'incomes': income_list
    }
    return render(request, "finance_app/income.html", context)