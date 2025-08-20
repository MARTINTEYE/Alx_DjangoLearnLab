from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegisterForm, ProfileForm, UserUpdateForm, PostForm
from .models import Post

# ------------------------
# Home / Index / Auth Views
# ------------------------

def home(request):
    return render(request, "blog/home.html")

def index(request):
    return render(request, "blog/index.html")

def register(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect("blog:profile")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect("blog:login")
    else:
        form = RegisterForm()
    return render(request, "blog/auth/register.html", {"form": form})

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
            return redirect("blog:profile")
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileForm(instance=user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "blog/auth/profile.html", context)


# ------------------------
# Blog Post CRUD Views
# ------------------------

# List all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]  # newest first

# Post detail view
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
