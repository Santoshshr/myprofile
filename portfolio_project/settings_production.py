"""
Production Django settings for portfolio_project.
Copy or symlink this file to your server and set appropriate environment variables.
"""
from .settings import *  # Import base settings
import os

# Force production defaults
DEBUG = False

# Replace these with your real domains / server IPs
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'your_domain.com www.your_domain.com 127.0.0.1').split()

# Static and Media
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Ensure WhiteNoise middleware is present (should be in base settings)
# Security settings
SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', '31536000'))
SECURE_SSL_REDIRECT = os.environ.get('DJANGO_SECURE_SSL_REDIRECT', 'True') == 'True'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Static files storage (already set in base settings to CompressedManifestStaticFilesStorage)

# Logging for production (appenders already set in base settings)
LOGGING['root']['level'] = os.environ.get('DJANGO_LOG_LEVEL', 'INFO')

# Database: you probably want to use PostgreSQL in production — configure via env vars
# Example (if using django-environ or DATABASE_URL): keep using DATABASES from base or override here.

# Additional production-ready settings
# Ensure templates load cached loaders in production for performance
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

# Additional middleware tuning for security
if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Final check: export DJANGO_SETTINGS_MODULE to point here in your systemd or environment
# export DJANGO_SETTINGS_MODULE=portfolio_project.settings_production
