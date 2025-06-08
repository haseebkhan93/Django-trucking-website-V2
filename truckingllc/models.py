from django.db import models

class QuoteRequest(models.Model):
    EQUIPMENT_CHOICES = [
        ('dry-van', "53' Dry Van"),
        ('reefer', 'Reefer'),
        ('flatbed', 'Flatbed'),
        ('power-only', 'Power Only'),
        ('hotshot', 'Hotshot'),
    ]

    broker_name = models.CharField(max_length=100)
    email = models.EmailField()
    pickup = models.CharField(max_length=200)
    dropoff = models.CharField(max_length=200)
    equipment = models.CharField(max_length=50, choices=EQUIPMENT_CHOICES)
    weight = models.PositiveIntegerField()
    pickup_date = models.DateField()
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.broker_name} - {self.pickup} to {self.dropoff}"

