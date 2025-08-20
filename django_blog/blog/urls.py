from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

app_name = "blog"

urlpatterns = [
    # Home / Index pages
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),

    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="blog/auth/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='blog:login'), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # Blog Post CRUD
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
