from django.urls import path
from . import views

# Define the URL patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('drivers/', views.drivers, name='drivers'),
    path('teams/', views.teams, name='teams'),
    path('races/', views.races, name='races'),
]