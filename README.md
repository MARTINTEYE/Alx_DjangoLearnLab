 API Authentication

This API uses Token Authentication. All write actions require a valid token.

Obtain Token
POST to `/api/auth/token/` with:
- username
- password

Returns:
```json
{"token": "your_token_here"}

