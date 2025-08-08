from rest_framework import generics, filters, permissions
from django_filters import rest_framework as drf_filters
from .models import Book
from .serializers import BookSerializer


# ------------------------------
# Custom permission: Authenticated users can write, others read-only
# ------------------------------
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to create, update, or delete.
    Read-only methods (GET, HEAD, OPTIONS) are open to all.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


# ------------------------------
# Filter setup for Book model
# ------------------------------
class BookFilter(drf_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author': ['exact', 'icontains'],
            'publication_year': ['exact', 'gte', 'lte'],
        }


# ------------------------------
# Generic API Views
# ------------------------------

# List all books
class BookListView(generics.ListAPIView):
    """
    GET: List all books with filtering, searching, and ordering.
    Accessible by everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [
        drf_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


# Retrieve one book
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book by ID.
    Accessible by everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Custom behavior during creation.
        Could link the current user if model has a created_by field.
        """
        serializer.save()


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Custom behavior during update.
        """
        serializer.save()


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
