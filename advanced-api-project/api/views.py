from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

#  List all books (Read Only - open to all)
class BookListView(generics.ListAPIView):
    """
    List all books.
    Accessible by both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


#  Retrieve a specific book by ID (Read Only)
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Accessible by both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


#  Create a new book (Authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Accessible only by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Customize behavior when creating a book.
        If Book model had a created_by field, you could assign:
        serializer.save(created_by=self.request.user)
        """
        serializer.save()


#  Update an existing book (Authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Accessible only by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Customize behavior during book update.
        """
        serializer.save()


#  Delete a book (Authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    Accessible only by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
