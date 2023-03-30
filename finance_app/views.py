from django.shortcuts import render, redirect
from django.utils import timezone
from finance_app.models import Purchase, Income
from .forms import IncomeForm, PurchaseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import statistics as stat


@login_required
def about_page(request):
    """View to load the about page"""
    return render(request, "finance_app/about.html")


@login_required
def purchase_page(request):
    """View to load the purchase page
       loads context into the page for the pieces of data
    """
    total_pur = sum([purchase.amount for purchase in Purchase.objects.all().filter(owner=request.user)])
    total_inc = sum([income.amount for income in Income.objects.all().filter(owner=request.user)])
    net = total_inc - total_pur
    if net < 0.001 and net > -0.001:
        net = 0
    
    context = {
        "title": "Purchases",
        'purchases': reversed(Purchase.objects.all()),
        'total': total_pur,
        'net': net
    }
    return render(request, "finance_app/purchases.html", context)


@login_required
def income_page(request):
    """View loads into the income page
       context loads the income objects into the html document for a nice, dynamic page
    """
    total_inc = sum([income.amount for income in Income.objects.all().filter(owner=request.user)])
    total_pur = sum([purchase.amount for purchase in Purchase.objects.all().filter(owner=request.user)])
    net = total_inc - total_pur
    if net < 0.001 and net > -0.001:
        net = 0
    
    context = {
        "title": "Income",
        'incomes': reversed(Income.objects.all()),
        'total': total_inc,
        'net': net
    }
    return render(request, "finance_app/income.html", context)


@login_required
def register_purchase(request):
    """ view to register purchase
        this view functions differently depending on whether the request is POST or GET
        if POST: register the data into the database and format it to be a Purchase
        if GET: produce a page with the empty form"""
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
    """ view to register income
        this view functions differently depending on whether the request is POST or GET
        if POST: register the data into the database and format it to be an Income
        if GET: produce a page with the empty form"""
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


@login_required
def income_charts(request):
    labels = []
    data = []
    
    for income in Income.objects.order_by("amount").filter(owner=request.user):
        labels.append(income.income_source)
        data.append(income.amount)
    
    context = {
        'labels': labels,
        'data': data
    }
    return render(request, "finance_app/income_charts.html", context)


@login_required
def purchase_charts(request):
    labels = []
    data = []
    
    for purchase in Purchase.objects.order_by("amount").filter(owner=request.user):
        labels.append(purchase.purchase_name)
        data.append(purchase.amount)

    context = {
        'labels': labels,
        'data': data
    }
    return render(request, "finance_app/purchase_charts.html", context)