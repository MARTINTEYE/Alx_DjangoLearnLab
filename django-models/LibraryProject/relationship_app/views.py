from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile
from django.views.generic import DetailView
from .models import Library

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.shortcuts import render

def register(request):
    return render(request, 'register.html')

from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Logic to add a book
    pass

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    # Logic to edit a book
    pass

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    # Logic to delete a book
    pass
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class BookDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/book_detail.html'  # Create this template
    context_object_name = 'book'