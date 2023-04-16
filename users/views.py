from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} has been registered!")
            return redirect("purchase_page")
    elif request.method =="GET":
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

@login_required
def profile(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "user": request.user,
        "update_user": user_form,
        "update_profile": profile_form,
    }
    return render(request, "users/profile.html", context)
