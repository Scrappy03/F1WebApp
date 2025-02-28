#!/usr/bin/env bash
# exit on error
set -o errexit

# Install pipenv if not already installed
pip install pipenv

# Install dependencies from Pipfile
pipenv install --deploy

# Activate the pipenv shell for subsequent commands
# This makes sure we're using the virtualenv created by pipenv
eval "$(pipenv --venv)/bin/activate"

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

echo "Build completed successfully!"
