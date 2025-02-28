"""
Simple script to check URL configuration.
Run this with: python url_check.py
"""
import os
import sys
import django

# Add the project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "f1app.settings")
django.setup()

# Check URLs
from django.urls import get_resolver
resolver = get_resolver()

print("Available URL patterns:")
for pattern in resolver.url_patterns:
    print(f"- {pattern.pattern}")

print("\nCheck if these URLs match your expectations.")
print("If not, review your urls.py files")
