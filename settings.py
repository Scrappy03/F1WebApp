# Import os for environment variables
import os
import dj_database_url

# Use environment variable for Secret Key in production
SECRET_KEY = os.environ.get('SECRET_KEY', 'local-dev-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
# For troubleshooting, temporarily set default to True, then revert after fixing
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Allow Render's domain and localhost
ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1',
    '.onrender.com',
    'apexdata.onrender.com',
]

# Add root URL configuration check
ROOT_URLCONF = 'f1app.urls'  # Make sure this is correct!

# Make sure static files are configured properly
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Render specific PostgreSQL database configuration
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            ssl_require=True
        )
    }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Right after security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Whitenoise static file settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'