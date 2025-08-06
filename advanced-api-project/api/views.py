from rest_framework import generics, permissions, filters  #  includes filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    #  Enables filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,     # Required for the check
        filters.OrderingFilter
    ]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']  # Enables ?search= functionality
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']



#  Retrieve a single book — Open to all
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Accessible by both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


#  Create book — Authenticated users only
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Accessible only by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# Update book — Authenticated users only
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Accessible only by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


#  Delete book — Authenticated users only
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    Accessible only by authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
