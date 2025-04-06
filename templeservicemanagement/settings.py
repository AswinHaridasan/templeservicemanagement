from pathlib import Path
import os
import pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
pymysql.install_as_MySQLdb()
# Security
SECRET_KEY = 'django-insecure-#z81_pa7#wb0iux)ie2iz#s$3_c$0n!_*kinarwyc0&it7wvlu'
DEBUG = False

ALLOWED_HOSTS = [
    "python-django-pgyd.onrender.com",  # Your Render app URL
    "localhost", 
    "127.0.0.1"
]

# Get PORT from environment variable (Render provides this)
PORT = os.getenv("PORT", "8000")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'temple',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'templeservicemanagement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates/'],
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

WSGI_APPLICATION = 'templeservicemanagement.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase_81yz',  # Extracted from URL
        'USER': 'mydatabase_81yz_user',  # Extracted from URL
        'PASSWORD': 'einzCmJ7usGD5ZINJItWap6pfuf2dM4s',  # Extracted from URL
        'HOST': 'dpg-cvmil2buibrs73bhmp20-a.oregon-postgres.render.com',  # Extracted from URL
        'PORT': '5432',  # Default PostgreSQL port
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_TRUSTED_ORIGINS = [
    "https://python-django-pgyd.onrender.com"
]



# Static and Media files
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Define STATIC_ROOT for production (important for deployment)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CERTIFICATES_DIR = os.path.join(MEDIA_ROOT, 'certificates')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Stripe Keys (Replace with actual keys)
STRIPE_PUBLIC_KEY = 'your-stripe-public-key'
STRIPE_SECRET_KEY = 'your-stripe-secret-key'

# Email Configuration (Do NOT hardcode credentials in production)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "aswinharidasan6777@gmail.com"
EMAIL_HOST_PASSWORD = "ycqyqszsgwvjbcaf"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Logging
LOGGING = {
    "version": 1,
    "handlers": {
        "mail_errors": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "email_errors.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["mail_errors"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
