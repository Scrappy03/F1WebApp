from django.contrib import admin
from .models import Driver, Team, Car, Circuit, Race, ChampionshipStandings, ConstructorStandings, QualifyingResult, SprintResult, RaceResult, Sponsor, Contract, PitStop, Penalty, DriverTeam, CarTeam

admin.site.register(Driver)
admin.site.register(Team)
admin.site.register(Car)
admin.site.register(Circuit)
admin.site.register(Race)
admin.site.register(ChampionshipStandings)
admin.site.register(ConstructorStandings)
admin.site.register(QualifyingResult)
admin.site.register(SprintResult)
admin.site.register(RaceResult)
admin.site.register(Sponsor)
admin.site.register(Contract)
admin.site.register(PitStop)
admin.site.register(Penalty)
admin.site.register(DriverTeam)
admin.site.register(CarTeam)