from django.contrib import admin
from .models import Vehicle, PriorityVehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'vehicle_type', 'speed', 'status', 'current_road', 'battery_level')
    list_filter = ('vehicle_type', 'status', 'current_road')
    search_fields = ('plate_number', 'destination')

@admin.register(PriorityVehicle)
class PriorityVehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'mission', 'priority_level', 'progress')
    list_filter = ('priority_level',)
    search_fields = ('vehicle__plate_number', 'mission')