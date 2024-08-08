from django.test import TestCase
from django.utils import timezone
from datetime import datetime

from theatre.models import Theatre, Performance


class TheatreModelTest(TestCase):
    def setUp(self):
        self.theatre = Theatre.objects.create(name="Teatro alla Scala", location="Milan, Italy")

    def test_theatre_creation(self):
        self.assertEqual(self.theatre.name, "Teatro alla Scala")
        self.assertEqual(self.theatre.location, "Milan, Italy")


class PerformanceModelTest(TestCase):
    def setUp(self):
        self.theatre = Theatre.objects.create(name="Royal Opera House", location="Govert Garden, London")
        self.start_time = timezone.make_aware(datetime(2024, 10, 5, 19, 0))
        self.end_time = timezone.make_aware(datetime(2024, 10, 5, 22, 0))
        self.performance = Performance.objects.create(
            name="La Traviata",
            description="An opera by Giuseppe Verdi.",
            start_time=self.start_time,
            end_time=self.end_time,
            theatre=self.theatre
        )

    def test_performance_creation(self):
        self.assertEqual(self.performance.name, "La Traviata")
        self.assertEqual(self.performance.description, "An opera by Giuseppe Verdi.")
        self.assertEqual(self.performance.theatre, self.theatre)
        self.assertEqual(self.performance.start_time, self.start_time)
        self.assertEqual(self.performance.end_time, self.end_time)
