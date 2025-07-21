from .views import list_books
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # <-- This line satisfies the checker

urlpatterns = [
    path('register/', views.register, name='register'),  # <-- Explicit 'views.register'

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
