from pathlib import Path
from decouple import config, Csv
import os

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Check if running on Railway (Railway sets multiple environment variables)
RAILWAY_ENV = (
    os.environ.get('RAILWAY_ENVIRONMENT') or 
    os.environ.get('RAILWAY_PROJECT_ID') or 
    os.environ.get('RAILWAY_SERVICE_ID') or
    'railway.app' in os.environ.get('RAILWAY_PUBLIC_DOMAIN', '')
)

# Security
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# Environment-specific ALLOWED_HOSTS
if RAILWAY_ENV:
    # Get the actual Railway domain from environment
    railway_domain = os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'django-trucking-website-production.up.railway.app')
    ALLOWED_HOSTS = [
        railway_domain,
        'django-trucking-website-production.up.railway.app',
        'django-trucking-website-production.railway.app', 
        '.railway.app',
        '*.railway.app',
        'localhost',
        '127.0.0.1'
    ]
else:
    # If Railway detection fails, use a broader approach
    ALLOWED_HOSTS = [
        'django-trucking-website-production.up.railway.app',
        'django-trucking-website-production.railway.app', 
        '.railway.app',
        '*.railway.app',
        'localhost',
        '127.0.0.1'
    ] + config('ALLOWED_HOSTS', default='').split(',')

# Environment-specific CSRF settings
if RAILWAY_ENV:
    # Get the actual Railway domain from environment
    railway_domain = os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'django-trucking-website-production.up.railway.app')
    
    CSRF_TRUSTED_ORIGINS = [
        f'https://{railway_domain}',
        'https://django-trucking-website-production.up.railway.app',
        'https://django-trucking-website-production.railway.app',
        'https://*.railway.app'
    ]
    
    # Additional CSRF settings for Railway
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SAMESITE = 'Lax'  # Important for Railway
    CSRF_USE_SESSIONS = False  # Use cookies instead of sessions
    
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Security headers
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = False  # Railway handles SSL termination
    
else:
    CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000']
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'truckingllc',  # Your main app
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serve static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'truckingwebsite.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'truckingwebsite.wsgi.application'

# Supabase Database (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': config('SUPABASE_USER'),
        'PASSWORD': config('SUPABASE_PASSWORD'),
        'HOST': 'aws-0-us-east-1.pooler.supabase.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
COMPANY_EMAIL = config('COMPANY_EMAIL')

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# WhiteNoise settings for better performance
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True if not RAILWAY_ENV else False

# Media files (if needed)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Additional security settings for production
if RAILWAY_ENV:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    
    # Performance settings
    WHITENOISE_MAX_AGE = 31536000  # 1 year cache for static files
    
    # Add logging configuration
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    }