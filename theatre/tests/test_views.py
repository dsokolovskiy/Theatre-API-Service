from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from datetime import datetime

from theatre.models import Theatre, Performance


class TheatreAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.theatre = Theatre.objects.create(
            name="National Theatre",
            location="Prague, Czech Republic"
        )
        self.url = "/api/theatres/"

    def test_theatre_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_theatre_create(self):
        data = {
            "name": "Theatre du Chatelet",
            "location": "Paris, France"
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Theatre du Chatelet")


class PerformanceAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.theatre = Theatre.objects.create(
            name="Theatre du Chatelet",
            location="Paris, France"
        )
        self.start_time = timezone.make_aware(datetime(2025, 1, 10, 18, 15))
        self.end_time = timezone.make_aware(datetime(2025, 1, 10, 20, 45))
        self.performance = Performance.objects.create(
            name="Madama Butterfly",
            description="An opera by Giacomo Puccini.",
            start_time=self.start_time,
            end_time=self.end_time,
            theatre=self.theatre
        )
        self.url = "/api/performances/"

    def test_performance_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_performance_create(self):
        data = {
            "name": "Rigoletto",
            "description": "An opera by Giuseppe Verdi.",
            "start_time": timezone.make_aware(datetime(
                2025, 2, 5, 17, 0)).isoformat(),
            "end_time": timezone.make_aware(datetime(
                2025, 2, 5, 19, 35)).isoformat(),
            "theatre": self.theatre.id
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Rigoletto")
