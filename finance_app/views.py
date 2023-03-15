from django.shortcuts import render, redirect
from django.utils import timezone
from finance_app.models import Purchase, Income
from .forms import IncomeForm, PurchaseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import statistics as stat


# creating dummy data to push to templates for testing

# purchase_list = [
#     {
#         'purchase_name': "Gasoline",
#         'purchase_description': "Gas for school",
#         'amount': 40.00,
#         'date_purchased': str(datetime.datetime.now()),
#         'owner': "smassnick24"
#     },
#     {
#         'purchase_name': "Snacks",
#         'purchase_description': "Snacks for aubrey",
#         'amount': 20.17,
#         'date_purchased': str(datetime.datetime.now()),
#         'owner': "smassnick24"
#     },
# ]

# income_list = [
#     {
#         "income_source": "Wesco",
#         "income_description": "paycheck from wesco",
#         "amount": 200.13,
#         "date_received": str(datetime.datetime.now()),
#         "owner": "smassnick24"
#     },
#     {
#         "income_source": "Wesco",
#         "income_description": "paycheck from wesco",
#         "amount": 313.13,
#         "date_received": str(datetime.datetime.now()),
#         "owner": "smassnick24"
#     }
# ]

@login_required
def purchase_page(request):
    context = {
        "title": "Purchases",
        'purchases': reversed(Purchase.objects.all())
    }
    return render(request, "finance_app/purchases.html", context)

@login_required
def income_page(request):
    context = {
        "title": "Income",
        'incomes': reversed(Income.objects.all())
    }
    return render(request, "finance_app/income.html", context)

@login_required
def register_purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase_n = form.cleaned_data.get('purchase_name')
            purchase_desc = form.cleaned_data.get('purchase_description')
            purchase_amount = form.cleaned_data.get('amount')
            user = request.user
            new_purchase = Purchase(purchase_name=purchase_n, purchase_description=purchase_desc, amount=purchase_amount, owner=user)
            new_purchase.save()
            messages.success(request, f"{purchase_n} has been inserted into the database!")
            return redirect("purchase_page")
    elif request.method =="GET":
        form = PurchaseForm()
    return render(request, "finance_app/register_income_data.html", {"form": form})

@login_required
def register_income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income_src = form.cleaned_data.get('income_source')
            income_desc = form.cleaned_data.get('income_description')
            income_total = form.cleaned_data.get('income')
            user = request.user
            new_income = Income(income_source=income_src, income_description=income_desc, amount=income_total, owner=user)
            new_income.save()
            messages.success(request, f"Payment from {income_src} has been inserted into the database!")
            return redirect("income_page")
    elif request.method =="GET":
        form = IncomeForm()
    return render(request, "finance_app/register_income_data.html", {"form": form})

@login_required
def income_statistics_page(request):
    """View to calculate simple statistics on income"""
    total_received = 0
    amount_list = []
    num_incomes = len(Income.objects.all().filter(owner=request.user))
    
    for income in Income.objects.all().filter(owner=request.user): # gathering data for computation
        total_received += income.amount
        amount_list.append(income.amount)
        
    amount_list.sort()
    
    income_mean = stat.mean(amount_list) # calculating the mean
    income_median = stat.median(amount_list) # calculating the median
    income_variance = stat.variance(amount_list) # calculating the variance
    income_std_dev = stat.stdev(amount_list) # calculating standard deviation
    
    context = {
        "title": "Statistics",
        "total_received": total_received,
        "mean_received": income_mean,
        "num_incomes": num_incomes,
        "median": income_median,
        "variance": income_variance,
        "standard_deviation": income_std_dev,
    }
    return render(request, "finance_app/income_statistics.html", context)

@login_required
def purchase_statistics_page(request):
    total_spent = 0
    amount_list = []
    num_purchases = len(Purchase.objects.all().filter(owner=request.user))
    
    for purchase in Purchase.objects.all().filter(owner=request.user): # gathering data for computation
        total_spent += purchase.amount
        amount_list.append(purchase.amount)
        
    amount_list.sort()
    
    purchase_mean = stat.mean(amount_list) # calculating the mean
    purchase_median = stat.median(amount_list) # calculating the median
    purchase_variance = stat.variance(amount_list) # calculating the variance
    purchase_std_dev = stat.stdev(amount_list) # calculating standard deviation
    
    context = {
        "title": "Statistics",
        "total_spent": total_spent,
        "num_purchases": num_purchases,
        "mean_spent": purchase_mean,
        "median": purchase_median,
        "variance": purchase_variance,
        "standard_deviation": purchase_std_dev,
    }
    return render(request, "finance_app/purchase_statistics.html", context)