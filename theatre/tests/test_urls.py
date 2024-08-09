from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from datetime import datetime

from theatre.models import Theatre, Performance
from theatre.views import TheatreViewSet, PerformanceViewSet
from django.contrib.auth.models import User


class TheatreURLTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.theatre = Theatre.objects.create(
            name="Royal Opera House",
            location="Govert Garden, London"
        )
        self.theatre_list_url = reverse("theatre-list")
        self.theatre_detail_url = reverse("theatre-detail", args=[self.theatre.id])

    def test_theatre_list_url_resolves(self):
        view = resolve(self.theatre_list_url)
        self.assertEqual(view.func.cls, TheatreViewSet)

    def test_theatre_detail_url_resolves(self):
        view = resolve(self.theatre_detail_url)
        self.assertEqual(view.func.cls, TheatreViewSet)

    def test_theatre_list_url(self):
        response = self.client.get(self.theatre_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_theatre_detail_url(self):
        response = self.client.get(self.theatre_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.theatre.name)


class PerformanceURLTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.theatre = Theatre.objects.create(
            name="The Sydney Opera House",
            location="Bennelong Point, Sydney"
        )
        self.start_time = timezone.make_aware(datetime(2024, 10, 12, 18, 20))
        self.end_time = timezone.make_aware(datetime(2024, 10, 12, 21, 30))
        self.performance = Performance.objects.create(
            name="The Phantom of the Opera",
            description="A musical with music by Andrew Lloyd Webber.",
            start_time=self.start_time,
            end_time=self.end_time,
            theatre=self.theatre
        )
        self.performance_list_url = reverse("performance-list")
        self.performance_detail_url = reverse("performance-detail", args=[self.performance.id])

    def test_performance_list_url_resolves(self):
        view = resolve(self.performance_list_url)
        self.assertEqual(view.func.cls, PerformanceViewSet)

    def test_performance_detail_url_resolves(self):
        view = resolve(self.performance_detail_url)
        self.assertEqual(view.func.cls, PerformanceViewSet)

    def test_performance_list_url(self):
        response = self.client.get(self.performance_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_detail_url(self):
        response = self.client.get(self.performance_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.performance.name)
