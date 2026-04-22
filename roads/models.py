from django.db import models
from django.core.validators import MinValueValidator

class Road(models.Model):
    DIRECTION_CHOICES = [
        ('ONE_WAY', 'One Way'),
        ('TWO_WAY', 'Two Way'),
    ]
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('MAINTENANCE', 'Maintenance'),
    ]

    name = models.CharField(max_length=255)
    zone = models.CharField(max_length=100)
    speed_limit = models.IntegerField(validators=[MinValueValidator(0)])
    direction = models.CharField(max_length=20, choices=DIRECTION_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return f"{self.name} ({self.zone})"

class Intersection(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    roads = models.ManyToManyField(Road, related_name='intersections')

    def __str__(self):
        return self.name