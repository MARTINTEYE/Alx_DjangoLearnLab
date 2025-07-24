"""
Django settings for advanced_features_and_security project.
"""

from pathlib import Path

# === BASE DIRECTORY ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === SECURITY ===
SECRET_KEY = 'django-insecure-h0cg7%*ab1yk0_gy4zapye8w1*no$#-1v^d^$73-%=&(hd8o@+'
DEBUG = False  # Never use DEBUG=True in production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Add your domain/IP in production

# === INSTALLED APPS ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'LibraryProject.bookshelf',
    'LibraryProject.accounts',
]

# === CUSTOM USER MODEL ===
AUTH_USER_MODEL = 'accounts.CustomUser'  

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# === MIDDLEWARE ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

# === URLS ===
ROOT_URLCONF = 'advanced_features_and_security.urls'

# === TEMPLATES ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# === WSGI ===
WSGI_APPLICATION = 'advanced_features_and_security.wsgi.application'

# === DATABASE ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === PASSWORD VALIDATORS ===
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# === INTERNATIONALIZATION ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === STATIC FILES ===
STATIC_URL = 'static/'

# === DEFAULT PRIMARY KEY ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === SECURITY SETTINGS ===

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Enforce HTTPS
SECURE_SSL_REDIRECT = True

# HSTS (Strict HTTPS)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Header protections
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# CSP (Content Security Policy)
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'https://fonts.googleapis.com')
CSP_SCRIPT_SRC = ("'self'",)
