# API Endpoints for Book Resource

# Routes

- GET `/api/books/` → List all books
- GET `/api/books/<id>/` → Get a specific book
- POST `/api/books/create/` → Add a new book (requires authentication)
- PUT `/api/books/<id>/update/` → Update an existing book (requires authentication)
- DELETE `/api/books/<id>/delete/` → Remove a book (requires authentication)

# Permissions
- Read operations are open to all users.
- Write operations require authentication.

# Notes
- Custom validation ensures `publication_year` is not in the future.
- Views are implemented using DRF's generic views for maintainability.
