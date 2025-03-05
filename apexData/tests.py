from django.test import TestCase
from .models import Driver, Team, Race, Circuit, ChampionshipStandings, QualifyingResult
from datetime import date, timedelta

# Create your tests here.

class DriverModelTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            first_name="Lewis",
            last_name="Hamilton",
            date_of_birth=date(1985, 1, 7),
            nationality="British",
            profile_image_url="https://example.com/image.jpg",
            driver_number=44,
            status='active'
        )

    def test_driver_creation(self):
        self.assertEqual(self.driver.first_name, "Lewis")
        self.assertEqual(self.driver.last_name, "Hamilton")
        self.assertEqual(self.driver.status, 'active')

    def test_driver_str(self):
        self.assertEqual(str(self.driver), "Lewis Hamilton")

class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            team_name="Mercedes AMG",
            principal_name="Toto Wolff",
            budget=500000000.00,
            base_location="Brackley",
            first_season=2010,
            logo_url="https://example.com/logo.jpg"
        )

    def test_team_creation(self):
        self.assertEqual(self.team.team_name, "Mercedes AMG")
        self.assertEqual(self.team.budget, 500000000.00)

    def test_team_str(self):
        self.assertEqual(str(self.team), "Mercedes AMG")

class ChampionshipStandingsTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            first_name="Max",
            last_name="Verstappen",
            date_of_birth=date(1997, 9, 30),
            nationality="Dutch",
            profile_image_url="https://example.com/max.jpg",
            driver_number=33,
            status='active'
        )
        self.standings = ChampionshipStandings.objects.create(
            season=2024,
            round_number=1,
            driver=self.driver,
            points=25,
            position=1
        )

    def test_standings_creation(self):
        self.assertEqual(self.standings.points, 25)
        self.assertEqual(self.standings.position, 1)

    def test_standings_str(self):
        self.assertEqual(str(self.standings), "2024 Round 1 - Max Verstappen")
