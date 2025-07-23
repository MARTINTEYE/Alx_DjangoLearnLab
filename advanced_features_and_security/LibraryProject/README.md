## Permissions and Groups Setup

This project uses Django's built-in permissions and groups system to manage access control.

### Custom Permissions (on Book model)
- `can_view`: Can view books
- `can_create`: Can add books
- `can_edit`: Can edit books
- `can_delete`: Can delete books

### Groups
- **Viewers**: Assigned `can_view`
- **Editors**: Assigned `can_view`, `can_create`, `can_edit`
- **Admins**: Assigned all permissions

### Usage in Views
Views use the `@permission_required()` decorator to enforce permissions.

Example:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
