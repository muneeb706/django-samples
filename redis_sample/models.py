from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    total_tickets = models.IntegerField()
    available_tickets = models.IntegerField()


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    customer_username = models.CharField(max_length=200)  # Simplified for this example
