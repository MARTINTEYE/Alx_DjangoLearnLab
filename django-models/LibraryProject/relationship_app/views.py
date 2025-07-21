from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.views.generic.detail import DetailView
from .models import Library, Book, UserProfile

# Role-based access control
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
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

# Registration view
def register(request):
    return render(request, 'register.html')

# Book permission views
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    pass  # Logic to add a book

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    pass  # Logic to edit a book

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    pass  # Logic to delete a book

# Function-based book list view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based views using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class BookDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/book_detail.html'
    context_object_name = 'book'
