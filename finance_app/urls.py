from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.finance_app, name="finance_app"),
    path("other", views.other_app, name="other_app"),
]