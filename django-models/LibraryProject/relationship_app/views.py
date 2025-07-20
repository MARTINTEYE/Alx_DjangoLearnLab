from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib import messages


# Register View
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in
            return redirect('home')  # Replace 'home' with your actual homepage URL name
        return render(request, 'relationship_app/register.html', {'form': form})


# Login View
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'relationship_app/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with your actual homepage URL name
        else:
            messages.error(request, 'Invalid username or password')
        return render(request, 'relationship_app/login.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
