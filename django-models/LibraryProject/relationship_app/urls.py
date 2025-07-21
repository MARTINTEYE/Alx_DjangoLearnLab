from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    register,
    list_books,
    add_book,
    edit_book,
    delete_book,
    BookDetailView,
    LibraryDetailView,
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    path('books/', list_books, name='list_books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
