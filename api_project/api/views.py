from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


# For listing books via GET /books/
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# For full CRUD via ViewSet and router (GET, POST, PUT, DELETE)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
