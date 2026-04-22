from django.contrib import admin
from .models import Road, Intersection

@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('name', 'zone', 'speed_limit', 'direction', 'status')
    list_filter = ('zone', 'direction', 'status')
    search_fields = ('name', 'zone')

@admin.register(Intersection)
class IntersectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    filter_horizontal = ('roads',)