from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm, UserUpdateForm

# Home page
def home(request):
    return render(request, "blog/home.html")

# Index page (optional landing page or blog feed)
def index(request):
    return render(request, "blog/index.html")

# User registration
def register(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect("profile")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect("login")
    else:
        form = RegisterForm()
    
    context = {"form": form}
    return render(request, "blog/auth/register.html", context)

# Profile view/update
@login_required
def profile(request):
    user = request.user

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileForm(instance=user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "blog/auth/profile.html", context)
