from rest_framework.routers import DefaultRouter

from django.urls import path, include
from theatre.views import (
    TheatreViewSet,
    PerformanceViewSet,
    SeatViewSet,
    ReservationViewSet,
    VisitorViewSet
)

router = DefaultRouter()
router.register(r"theatres", TheatreViewSet)
router.register(r"performances", PerformanceViewSet)
router.register(r"seats", SeatViewSet)
router.register(r"reservations", ReservationViewSet)
router.register(r"visitors", VisitorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
