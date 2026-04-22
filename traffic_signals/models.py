from django.db import models
from django.core.validators import MinValueValidator
from roads.models import Intersection

class TrafficSignal(models.Model):
    STATE_CHOICES = [
        ('RED', 'Red'),
        ('ORANGE', 'Orange'),
        ('GREEN', 'Green'),
    ]
    MODE_CHOICES = [
        ('FIXED', 'Fixed'),
        ('ADAPTIVE', 'Adaptive'),
    ]

    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE, related_name='traffic_signals')
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='RED')
    cycle_duration = models.PositiveIntegerField(help_text="Cycle duration in seconds", validators=[MinValueValidator(1)])
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='FIXED')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Signal at {self.intersection.name} ({self.get_state_display()})"