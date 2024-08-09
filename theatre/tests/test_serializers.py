from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

from theatre.models import Theatre, Performance
from theatre.serializers import TheatreSerializer, PerformanceSerializer


class TheatreSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.theatre = Theatre.objects.create(
            name="Vienna State Opera",
            location="Vienna, Austria"
        )
        self.url = "/api/theatres/{}/".format(self.theatre.id)

    def test_theatre_serializer_get(self):
        response = self.client.get(self.url)
        serializer = TheatreSerializer(self.theatre)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_theatre_serializer_post(self):
        data = {
            "name": "New Theatre",
            "location": "Berlin, Germany"
        }
        response = self.client.post("/api/theatres/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Theatre")

    def test_theatre_serializer_put(self):
        data = {
            "name": "Updated Theatre",
            "location": "Berlin, Germany"
        }
        response = self.client.put(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Theatre")

    def test_theatre_serializer_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PerformanceSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

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

    def test_performance_serializer_get(self):
        response = self.client.get(self.url)
        serializer = PerformanceSerializer(self.performance)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_performance_serializer_post(self):
        data = {
            "name": "New Performance",
            "description": "A new performance description.",
            "start_time": "2025-02-06T18:00:00Z",
            "end_time": "2025-02-06T20:00:00Z",
            "theatre": self.theatre.id
        }
        response = self.client.post("/api/performances/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Performance")

    def test_performance_serializer_put(self):
        data = {
            "name": "Updated Performance",
            "description": "An updated description.",
            "start_time": "2025-02-06T18:00:00Z",
            "end_time": "2025-02-06T20:00:00Z",
            "theatre": self.theatre.id
        }
        response = self.client.put(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Performance")

    def test_performance_serializer_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
