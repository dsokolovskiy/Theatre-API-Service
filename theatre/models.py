from django.db import models


class Theatre(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="theatres/", null=True, blank=True)

    def __str__(self):
        return self.name


class Performance(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name="performances")
    image = models.ImageField(upload_to="performances", null=True, blank=True)

    def __str__(self):
        return self.name


class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seat_number} for {self.performance.name}"


class Reservation(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    visitor = models.ForeignKey("Visitor", on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.visitor.name} on {self.reservation_date}"


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
