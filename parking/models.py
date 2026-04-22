from django.db import models
from django.core.validators import MinValueValidator

class Parking(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    occupied_places = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.00)])
    charging_station = models.BooleanField(default=False)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.occupied_places > self.capacity:
            raise ValidationError('Occupied places cannot exceed capacity.')

    def __str__(self):
        return f"{self.name} ({self.occupied_places}/{self.capacity})"