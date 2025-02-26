from django.shortcuts import render
from django.http import HttpResponse
from .models import Driver, DriverTeam

# Create your views here.
def index(request):
    drivers = Driver.objects.all()
    context = {'drivers': drivers}
    return render(request, 'index.html', context)

def drivers(request):
    drivers = Driver.objects.all().order_by('points').reverse()
    driver_teams = DriverTeam.objects.select_related('team').all()
    context = {
        'drivers': drivers,
        'driver_teams': driver_teams
    }
    return render(request, 'drivers.html', context)

def teams(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'teams.html', context)

def races(request):
    return render(request, 'races.html')