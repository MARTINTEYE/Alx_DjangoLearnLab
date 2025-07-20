from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, home_view

urlpatterns = [
    path('', home_view, name='home'),  # Your homepage view
    path('login/', auth_views.LoginView.as_view(
        template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

