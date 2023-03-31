from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("purchase", views.purchase_page, name="purchase_page"),
    path("income", views.income_page, name="income_page"),
    path("income_statistics", views.income_statistics_page, name="income_statistics_page"),
    path("purchase_statistics", views.purchase_statistics_page, name="purchase_statistics_page"),
    path("about", views.about_page, name="about"),
    path("income_charts", views.income_charts, name="income_charts_page"),
    path("purchase_charts", views.purchase_charts, name="purchase_charts_page"),
    path("", views.landing, name="landing")
]