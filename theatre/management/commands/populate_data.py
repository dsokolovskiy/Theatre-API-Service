from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime

from theatre.models import Theatre, Performance


class Command(BaseCommand):
    help = "Populate database with initial data"

    def handle(self, *args, **kwargs):
        theatre1 = Theatre.objects.create(name="Teatro Real de Madrid", location="Calle de Arrieta, Madrid")
        theatre2 = Theatre.objects.create(name="The Sydney Opera House", location="Bennelong Point, Sydney")

        start_time1 = timezone.make_aware(datetime(2024, 9, 27, 17, 30))
        end_time1 = timezone.make_aware(datetime(2024, 9, 27, 20, 30))
        start_time2 = timezone.make_aware(datetime(2024, 10, 12, 18, 20))
        end_time2 = timezone.make_aware(datetime(2024, 10, 12, 21, 30))

        Performance.objects.create(
            name="Hamlet",
            description="A tragedy written by William Shakespeare.",
            start_time=start_time1,
            end_time=end_time1,
            theatre=theatre1,
        )
        Performance.objects.create(
            name="The Phantom of the Opera",
            description="A musical with music by Andrew Lloyd Webber.",
            start_time=start_time2,
            end_time=end_time2,
            theatre=theatre2,
        )
        self.stdout.write(self.style.SUCCESS("Successfully populated the database"))
