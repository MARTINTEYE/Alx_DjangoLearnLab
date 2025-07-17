import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  
    except Author.DoesNotExist:
        return "Author not found"

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return "Library not found"
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # <-- required line!
        return librarian
    except Library.DoesNotExist:
        return "Library not found"
    except Librarian.DoesNotExist:
        return "No librarian assigned"

if __name__ == "__main__":
    print("Books by author:", books_by_author("John Doe"))
    print("Books in library:", books_in_library("Central Library"))
    print("Librarian:", librarian_for_library("Central Library"))
