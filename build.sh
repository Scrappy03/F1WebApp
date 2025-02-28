#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Starting build process ==="

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories if they don't exist
echo "Ensuring static directory exists..."
mkdir -p static/styles

# Verify CSS file location before collectstatic
echo "=== Checking CSS file before collectstatic ==="
find . -name "styles.css"

# Collect static files with verbose output
echo "Collecting static files..."
python manage.py collectstatic --no-input -v 2

# Verify CSS file location after collectstatic
echo "=== Checking CSS file after collectstatic ==="
find staticfiles -name "styles.css"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Print out installed packages for debugging
echo "=== Installed Python packages ==="
pip freeze

# Print Django version
echo "=== Django version ==="
python -c "import django; print(django.get_version())"

# List all files in staticfiles directory
echo "=== Files in staticfiles directory ==="
find staticfiles -type f | sort

echo "Build completed successfully!"