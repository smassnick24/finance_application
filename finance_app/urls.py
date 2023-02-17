from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("purchase", views.purchase_page, name="purchase_page"),
    path("income", views.income_page, name="income_page"),
]