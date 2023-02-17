from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def finance_app(request):
    return render(request, "finance_app/home.html")

def other_app(request):
    return render(request, "finance_app/about.html")