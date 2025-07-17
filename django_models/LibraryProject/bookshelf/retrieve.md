```python
book = Book.objects.get(title="1984")
book.title             # '1984'
book.author            # 'George Orwell'
book.publication_year  # 1949


#Expected Output
'1984'
'George Orwell'
1949
