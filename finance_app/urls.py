from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.purchase_page, name="purchase_page"),
    path("income", views.income_page, name="income_page"),
    path("income_statistics", views.income_statistics_page, name="income_statistics_page"),
    path("purchase_statistics", views.purchase_statistics_page, name="purchase_statistics_page"),
]