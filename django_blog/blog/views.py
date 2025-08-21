# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import RegisterForm, ProfileForm, UserUpdateForm, PostForm, CommentForm
from .models import Post, Comment, Tag

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

    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created! You can now log in.")
        return redirect("blog:login")

    return render(request, "blog/auth/register.html", {"form": form})

@login_required
def profile(request):
    user = request.user
    u_form = UserUpdateForm(request.POST or None, instance=user)
    p_form = ProfileForm(request.POST or None, request.FILES or None, instance=user.profile)

    if request.method == "POST" and u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("blog:profile")

    return render(request, "blog/auth/profile.html", {"u_form": u_form, "p_form": p_form})


# ------------------------
# Blog Post CRUD Views
# ------------------------
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]  # newest first

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        return self.request.user == self.get_object().author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:index")

    def test_func(self):
        return self.request.user == self.get_object().author


# ------------------------
# Comment CRUD Views
# ------------------------
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comments/comment_form.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comments/comment_form.html"

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comments/comment_confirm_delete.html"

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


# ------------------------
# Tagging & Search Views
# ------------------------
def posts_by_tag(request, tag_name):
    tag = Tag.objects.filter(name=tag_name).first()
    posts = tag.posts.all() if tag else Post.objects.none()
    return render(request, "blog/post_list.html", {"posts": posts, "filter_tag": tag_name})

def search_posts(request):
    query = request.GET.get("q", "")
    posts = Post.objects.none()
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, "blog/search_results.html", {"posts": posts, "query": query})

class PostByTagListView(ListView):
    model = Post
    template_name = "blog/post_list.html"   # reuse your post list template
    context_object_name = "posts"

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[self.tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context