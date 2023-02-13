from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def finance_app(request):
    return HttpResponse("<h1>Hello World</h1>")

def other_app(request):
    return HttpResponse("<h1>App 2</h1>")