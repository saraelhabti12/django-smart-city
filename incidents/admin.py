from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('title', 'incident_type', 'severity', 'status', 'road', 'created_at')
    list_filter = ('incident_type', 'severity', 'status', 'road')
    search_fields = ('title', 'road__name')
    readonly_fields = ('created_at',)