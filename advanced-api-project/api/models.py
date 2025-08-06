from django.db import models

class Author(models.Model):
    """
    The Author model represents a book author.
    Each author can be associated with multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    The Book model represents a published book.
    Each book is associated with a single author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
