from rest_framework import viewsets, filters

from theatre.models import (
    Theatre,
    Performance,
    Seat,
    Reservation,
    Visitor, Review
)

from theatre.serializers import (
    TheatreSerializer,
    PerformanceSerializer,
    SeatSerializer,
    ReservationSerializer,
    VisitorSerializer, ReviewSerializer
)


class TheatreViewSet(viewsets.ModelViewSet):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ("name", "description")
    ordering_fields = "__all__"
    ordering = ["start_time"]


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
