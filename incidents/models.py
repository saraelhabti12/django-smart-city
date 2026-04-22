from django.db import models
from roads.models import Road

class Incident(models.Model):
    TYPE_CHOICES = [
        ('ACCIDENT', 'Accident'),
        ('TRAFFIC_JAM', 'Traffic Jam'),
        ('ROAD_WORK', 'Road Work'),
        ('HAZARD', 'Hazard'),
        ('OTHER', 'Other'),
    ]
    SEVERITY_CHOICES = [
        ('MINOR', 'Minor'),
        ('MODERATE', 'Moderate'),
        ('SEVERE', 'Severe'),
        ('CRITICAL', 'Critical'),
    ]
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('RESOLVING', 'Resolving'),
        ('RESOLVED', 'Resolved'),
    ]

    title = models.CharField(max_length=255)
    incident_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    road = models.ForeignKey(Road, on_delete=models.CASCADE, related_name='incidents')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.get_severity_display()} ({self.road.name})"