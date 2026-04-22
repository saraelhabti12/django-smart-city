from django.contrib import admin
from .models import Parking

@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'occupied_places', 'price', 'charging_station')
    list_filter = ('charging_station',)
    search_fields = ('name',)