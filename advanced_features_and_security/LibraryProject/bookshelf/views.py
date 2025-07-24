from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # book creation logic here
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # book edit logic here
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # book delete logic here
    pass

def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.none()
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.shortcuts import render
from .forms import BookForm

def form_example_view(request):
    form = BookForm()  # Validates and sanitizes user input using Django forms

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Prevents SQL injection by not using raw SQL
            form.save()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})
