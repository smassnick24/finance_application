from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from finance_app import views as finance_views

urlpatterns = [
    path("", include("finance_app.urls")),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('new_income/', finance_views.register_income, name="register_new_income"),
    path('new_purchase/', finance_views.register_purchase, name="register_new_purchase"),
    path('admin/', admin.site.urls),
]
