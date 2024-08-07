from django.contrib import admin

from theatre.models import (
    Theatre,
    Performance,
    Seat,
    Reservation,
    Visitor
)


@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("name", "theatre", "start_time", "end_time")


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("seat_number", "performance", "is_reserved", "is_vip")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("seat", "visitor", "reservation_date")


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
