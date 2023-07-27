from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    # Standard function for displaying information about model
    def __str__(self):
        return f"{self.city} ({self.code})"

# Flight inherits from models.Model; thus Flight is a model
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # Standard function for displaying information about model
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

    # Ensure flight is valid
    def is_valid_flight(self):
        return self.origin != self.destination and self.duration > 0

class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    # Standard function for displaying information about model
    def __str__(self):
        return f"{self.first_name} {self.last_name}"