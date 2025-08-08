from rest_framework import generics, filters
from django_filters import rest_framework as django_filters
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Protect endpoint
    filter_backends = [
        django_filters.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    # Filter by specific fields
    filterset_fields = ['title', 'author', 'publication_year']
    # Allow ordering by these fields
    ordering_fields = ['title', 'author', 'publication_year']
    # Allow search in these fields
    search_fields = ['title', 'author']
