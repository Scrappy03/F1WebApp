from django.db import models
from django.core.validators import URLValidator

# Create your models here.

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)
    points = models.IntegerField(default=0, verbose_name='Current Season Points')
    career_points = models.IntegerField(default=0)
    championships_won = models.IntegerField(default=0)
    total_race_wins = models.IntegerField(default=0)
    profile_image_url = models.URLField(validators=[URLValidator()])
    driver_number = models.IntegerField()
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('reserve', 'Reserve'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255)
    principal_name = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    constructor_points = models.IntegerField(default=0)
    championships_won = models.IntegerField(default=0)
    logo_url = models.URLField(validators=[URLValidator()])
    base_location = models.CharField(max_length=255)
    first_season = models.IntegerField()
    drivers = models.ManyToManyField(Driver, through='DriverTeam')

    def __str__(self):
        return self.team_name

class Car(models.Model):
    car_model = models.CharField(primary_key=True, max_length=255)
    engine_type = models.CharField(max_length=255)
    horsepower = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    year_manufactured = models.IntegerField()
    teams = models.ManyToManyField(Team, through='CarTeam')

    def __str__(self):
        return self.car_model

class Circuit(models.Model):
    circuit_id = models.AutoField(primary_key=True)
    circuit_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    track_length = models.DecimalField(max_digits=5, decimal_places=2)
    total_laps = models.IntegerField()
    circuit_map_url = models.URLField(validators=[URLValidator()])
    number_of_drs_zones = models.IntegerField()
    lap_record = models.DurationField()
    lap_record_holder = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    first_grand_prix = models.IntegerField()

    def __str__(self):
        return self.circuit_name

class Race(models.Model):
    race_id = models.AutoField(primary_key=True)
    race_name = models.CharField(max_length=255)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    date = models.DateField()
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    race_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    weather_conditions = models.CharField(max_length=255)
    safety_car_deployments = models.IntegerField(default=0)
    red_flag_deployments = models.IntegerField(default=0)
    sprint_race = models.BooleanField(default=False)
    season = models.IntegerField()
    round_number = models.IntegerField()

    class Meta:
        unique_together = ['season', 'round_number']

    def __str__(self):
        return f"{self.race_name} {self.season}"

class ChampionshipStandings(models.Model):
    season = models.IntegerField()
    round_number = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    points = models.IntegerField()
    position = models.IntegerField()
    wins = models.IntegerField(default=0)
    podiums = models.IntegerField(default=0)
    dnfs = models.IntegerField(default=0)

    class Meta:
        unique_together = ['season', 'round_number', 'driver']

    def __str__(self):
        return f"{self.season} Round {self.round_number} - {self.driver}"

class ConstructorStandings(models.Model):
    season = models.IntegerField()
    round_number = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        unique_together = ['season', 'round_number', 'team']

    def __str__(self):
        return f"{self.season} Round {self.round_number} - {self.team}"

class QualifyingResult(models.Model):
    qualifying_id = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    q1_time = models.DurationField(null=True, blank=True)
    q2_time = models.DurationField(null=True, blank=True)
    q3_time = models.DurationField(null=True, blank=True)
    final_position = models.IntegerField()

    class Meta:
        unique_together = ['race', 'driver']

    def __str__(self):
        return f"{self.race} - {self.driver} - P{self.final_position}"

class SprintResult(models.Model):
    sprint_id = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    position = models.IntegerField()
    points_earned = models.IntegerField()

    class Meta:
        unique_together = ['race', 'driver']

    def __str__(self):
        return f"{self.race} Sprint - {self.driver} - P{self.position}"

class RaceResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    position = models.IntegerField()
    laps_completed = models.IntegerField()
    fastest_time = models.DurationField()
    grid_position = models.IntegerField()
    points_earned = models.IntegerField()
    dnf_status = models.BooleanField(default=False)
    dnf_reason = models.CharField(max_length=255, null=True, blank=True)
    gap_to_leader = models.DurationField(null=True, blank=True)
    number_of_pit_stops = models.IntegerField(default=0)

    class Meta:
        unique_together = ['race', 'position']

    def __str__(self):
        return f"{self.race} - {self.driver} - P{self.position}"

# Keep the existing supporting models
class Sponsor(models.Model):
    sponsor_id = models.AutoField(primary_key=True)
    sponsor_name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    contribution_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.sponsor_name

class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.driver} - {self.start_date} to {self.end_date}"

class PitStop(models.Model):
    pit_stop_id = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    lap_number = models.IntegerField()
    pit_stop_time = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.race} - {self.driver} - Lap {self.lap_number}"

class Penalty(models.Model):
    penalty_id = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    time_penalty = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.race} - {self.driver} - {self.reason}"

class DriverTeam(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['driver', 'team']

    def __str__(self):
        return f"{self.driver} - {self.team}"

class CarTeam(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, to_field='car_model')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['car', 'team']

    def __str__(self):
        return f"{self.car} - {self.team}"