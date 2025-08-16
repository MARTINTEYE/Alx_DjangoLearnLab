from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already registered and logged in.")
        return redirect('profile')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'blog/profile.html', context)

# Optional: If you want to subclass Login/Logout for custom behavior, you can,
# but using auth_views directly in urls is fine.
