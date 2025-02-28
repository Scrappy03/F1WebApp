# Import os for environment variables
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
# Use environment variable for Secret Key in production
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-local-dev-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allow Render's domain and localhost
ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1',
    '.onrender.com',  # Allow all subdomains of onrender.com
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Render specific PostgreSQL database configuration
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            ssl_require=True
        )
    }

# Add whitenoise for static files
MIDDLEWARE = [
    # ...existing middleware...
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...existing middleware...
]

# Whitenoise static file settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
