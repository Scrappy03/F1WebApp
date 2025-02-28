from django.shortcuts import render
from django.http import HttpResponse
from .models import Driver, DriverTeam, Team

# Create your views here.
def index(request):
    drivers = Driver.objects.all()
    context = {'drivers': drivers}
    return render(request, 'index.html', context)

def drivers(request):
    drivers = Driver.objects.all().order_by('-points')  # Note the - for descending order
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

def standings(request):
    # Get drivers ordered by points (highest first)
    drivers = Driver.objects.all().order_by('-points')
    driver_teams = DriverTeam.objects.select_related('team').all()
    
    # Create standings data from drivers
    standings_data = []
    for position, driver in enumerate(drivers, 1):
        driver_team = next((dt for dt in driver_teams if dt.driver_id == driver.driver_id), None)
        
        standings_data.append({
            'position': position,
            'driver_name': f"{driver.first_name} {driver.last_name}",
            'number': driver.driver_number,
            'team_name': driver_team.team.team_name if driver_team else 'Unknown',
            'points': driver.points,
            'wins': driver.wins,
            'podiums': driver.podiums,
            'dnfs': driver.dnfs
        })
    
    return render(request, 'standings.html', {'standings': standings_data})