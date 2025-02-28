#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Starting build process ==="

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Collect static files with verbose output
echo "Collecting static files..."
python manage.py collectstatic --no-input -v 2

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Print out installed packages for debugging
echo "=== Installed Python packages ==="
pip freeze

echo "Build completed successfully!"