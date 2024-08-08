from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime

from theatre.models import Theatre, Performance


class Command(BaseCommand):
    help = "Populate database with initial data"

    def handle(self, *args, **kwargs):
        theatre1, created = Theatre.objects.get_or_create(
            name="Teatro Real de Madrid",
            defaults={"location": "Calle de Arrieta, Madrid"}
        )
        theatre2, created = Theatre.objects.get_or_create(
            name="The Sydney Opera House",
            defaults={"location": "Bennelong Point, Sydney"}
        )
        theatre3, created = Theatre.objects.get_or_create(
            name="Teatro alla Scala",
            defaults={"location": "Milan, Italy"}
        )
        theatre4, created = Theatre.objects.get_or_create(
            name="Royal Opera House",
            defaults={"location": "Govert Garden, London"}
        )
        theatre5, created = Theatre.objects.get_or_create(
            name="Vienna State Opera",
            defaults={"location": "Vienna, Austria"}
        )
        theatre6, created = Theatre.objects.get_or_create(
            name="Metropolitan Opera House",
            defaults={"location": "New York City, USA"}
        )
        theatre7, created = Theatre.objects.get_or_create(
            name="National Theatre",
            defaults={"location": "Prague, Czech Republic"}
        )

        performance_data = [
            {
                "name": "Hamlet",
                "description": "A tragedy written by William Shakespeare.",
                "start_time": timezone.make_aware(datetime(2024, 9, 27, 17, 30)),
                "end_time": timezone.make_aware(datetime(2024, 9, 27, 20, 30)),
                "theatre": theatre1
            },
            {
                "name": "The Phantom of the Opera",
                "description": "A musical with music by Andrew Lloyd Webber.",
                "start_time": timezone.make_aware(datetime(2024, 10, 12, 18, 20)),
                "end_time": timezone.make_aware(datetime(2024, 10, 12, 21, 30)),
                "theatre": theatre2
            },
            {
                "name": "Carmen",
                "description": "An opera in four acts by French composer Georges Bizet.",
                "start_time": timezone.make_aware(datetime(2024, 11, 15, 19, 45)),
                "end_time": timezone.make_aware(datetime(2024, 11, 15, 22, 45)),
                "theatre": theatre3
            },
            {
                "name": "La Traviata",
                "description": "An opera in three acts by Giuseppe Verdi.",
                "start_time": timezone.make_aware(datetime(2024, 12, 20, 20, 10)),
                "end_time": timezone.make_aware(datetime(2024, 12, 20, 23, 00)),
                "theatre": theatre4
            },
            {
                "name": "Don Giovanni",
                "description": "An opera in two acts by Wolfgang Amadeus Mozart.",
                "start_time": timezone.make_aware(datetime(2025, 1, 10, 18, 15)),
                "end_time": timezone.make_aware(datetime(2025, 1, 10, 20, 45)),
                "theatre": theatre5
            },
            {
                "name": "Aida",
                "description": "An opera in four acts by Giuseppe Verdi.",
                "start_time": timezone.make_aware(datetime(2025, 2, 5, 17, 00)),
                "end_time": timezone.make_aware(datetime(2025, 2, 5, 19, 35)),
                "theatre": theatre6
            },
            {
                "name": "La Boheme",
                "description": "An opera in four acts by Giacomo Puccini.",
                "start_time": timezone.make_aware(datetime(2025, 4, 14, 19, 10)),
                "end_time": timezone.make_aware(datetime(2025, 4, 14, 21, 40)),
                "theatre": theatre7
            }
        ]

        for data in performance_data:
            Performance.objects.get_or_create(
                name=data["name"],
                defaults={
                    "description": data["description"],
                    "start_time": data["start_time"],
                    "end_time": data["end_time"],
                    "theatre": data["theatre"]
                }
            )

        self.stdout.write(self.style.SUCCESS(
            "Successfully populated the database with theatres & performances"))
