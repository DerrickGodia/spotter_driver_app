from django.conf import settings
from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Server(models.Model):
    pass


class Truck(models.Model):
    truck_registration = models.CharField(max_length=30)

    def __str__(self):
        return self.truck_registration


class Trailer(models.Model):
    trailer_registration = models.CharField(max_length=30)

    def __str__(self):
        return self.trailer_registration


class Trip(models.Model):
    name = models.CharField(max_length=100)
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="trip_driver",
    )
    truck = models.ForeignKey(
        Truck, on_delete=models.CASCADE, related_name="trip_truck"
    )
    trailer = models.ForeignKey(
        Trailer, on_delete=models.CASCADE, related_name="trip_trailer"
    )
    start_time = models.DateTimeField()
    start_location = models.CharField(max_length=100)
    pick_location = models.CharField(max_length=100)
    drop_location = models.CharField(max_length=100)
    trip_manifest = models.CharField(max_length=100)
    trip_commodity = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Journey(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="trip_id")
    journey_location = models.CharField(max_length=100)
    journey_type = models.CharField(max_length=30)
    break_start_time = models.DateTimeField()
    break_end_time = models.DateTimeField()
    duration = models.DurationField()

    def save(self, *args, **kwargs):
        self.duration = self.break_end_time - self.break_start_time
        super().save(*args, **kwargs)

    def __str__(self):
        return self.journey_location
