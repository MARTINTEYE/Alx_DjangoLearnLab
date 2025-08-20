from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

app_name = "blog"

# ------------------------
# Home / Index
# ------------------------
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
]

# ------------------------
# Authentication
# ------------------------
urlpatterns += [
    path("login/", auth_views.LoginView.as_view(template_name="blog/auth/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='blog:login'), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]

# ------------------------
# Blog Post CRUD
# ------------------------
urlpatterns += [
    path("post/", PostListView.as_view(), name="post-list"),               # list all posts
    path("post/new/", PostCreateView.as_view(), name="post-create"),       # create a new post
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # view post
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # update post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),  # delete post
]

# ------------------------
# Comments
# ------------------------
# Comments
urlpatterns += [
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
