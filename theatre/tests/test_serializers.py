from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone

from datetime import datetime

from theatre.models import Theatre, Performance
from theatre.serializers import TheatreSerializer, PerformanceSerializer


class TheatreSerializerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.theatre = Theatre.objects.create(
            name="Vienna State Opera",
            location="Vienna, Austria"
        )
        self.url = "/api/theatres/{}/".format(self.theatre.id)

    def test_theatre_serializer(self):
        response = self.client.get(self.url)
        serializer = TheatreSerializer(self.theatre)
        self.assertEqual(response.data, serializer.data)


class PerformanceSerializerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.theatre = Theatre.objects.create(
            name="Metropolitan Opera House",
            location="New York City, USA"
        )
        self.start_time = timezone.make_aware(datetime(2025, 2, 5, 17, 0))
        self.end_time = timezone.make_aware(datetime(2025, 2, 5, 19, 35))
        self.performance = Performance.objects.create(
            name="Carmen",
            description="An opera by Georges Bizet.",
            start_time=self.start_time,
            end_time=self.end_time,
            theatre=self.theatre,
        )
        self.url = "/api/performances/{}/".format(self.performance.id)

    def test_performance_serializer(self):
        response = self.client.get(self.url)
        serializer = PerformanceSerializer(self.performance)
        self.assertEqual(response.data, serializer.data)
