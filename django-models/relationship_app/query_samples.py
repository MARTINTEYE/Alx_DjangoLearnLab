from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (e.g., author with id=1)
books_by_author = Book.objects.filter(author_id=1)

# 2. List all books in a library (e.g., library with id=1)
library = Library.objects.get(id=1)
books_in_library = library.books.all()

# 3. Retrieve the librarian for a library (e.g., library with id=1)
librarian = Librarian.objects.get(library_id=1)

# Display results
print("Books by Author:", books_by_author)
print("Books in Library:", books_in_library)
print("Librarian:", librarian.name)
