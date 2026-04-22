from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from roads.models import Road

class Vehicle(models.Model):
    TYPE_CHOICES = [
        ('CAR', 'Car'),
        ('BUS', 'Bus'),
        ('TRUCK', 'Truck'),
        ('MOTORCYCLE', 'Motorcycle'),
        ('EMERGENCY', 'Emergency'),
    ]
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('PARKED', 'Parked'),
        ('CHARGING', 'Charging'),
        ('MAINTENANCE', 'Maintenance'),
    ]

    plate_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    speed = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    current_road = models.ForeignKey(Road, on_delete=models.SET_NULL, null=True, blank=True, related_name='vehicles')
    battery_level = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], help_text="Battery level percentage")
    destination = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.plate_number} ({self.get_vehicle_type_display()})"

class PriorityVehicle(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name='priority_info')
    mission = models.CharField(max_length=255)
    priority_level = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    progress = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], help_text="Mission progress percentage")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.vehicle.plate_number} - {self.mission} ({self.priority_level})"