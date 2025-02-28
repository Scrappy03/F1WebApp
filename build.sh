#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Starting build process ==="

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Print out installed packages for debugging
echo "=== Installed Python packages ==="
pip freeze

# Print Django version
echo "=== Django version ==="
python -c "import django; print(django.get_version())"

# Check if wsgi.py exists
echo "=== Checking for WSGI file ==="
if [ -f "f1app/wsgi.py" ]; then
    echo "f1app/wsgi.py exists"
else
    echo "WARNING: f1app/wsgi.py does not exist. Check your project structure!"
    find . -name "wsgi.py"
fi

echo "Build completed successfully!"