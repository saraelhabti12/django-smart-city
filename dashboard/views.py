from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import F, Count
from vehicles.models import Vehicle, PriorityVehicle
from incidents.models import Incident
from roads.models import Road
from parking.models import Parking
import json

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = 'login'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Live counters
        context['total_vehicles'] = Vehicle.objects.count()
        context['active_incidents'] = Incident.objects.filter(status='ACTIVE').count()
        context['total_roads'] = Road.objects.count()
        context['busy_parkings'] = Parking.objects.filter(occupied_places__gte=F('capacity') * 0.8).count()
        context['priority_missions'] = PriorityVehicle.objects.exclude(progress=100).count()
        
        # Vehicles by type
        vehicle_types = Vehicle.objects.values('vehicle_type').annotate(count=Count('id'))
        context['vehicles_by_type_labels'] = json.dumps([v['vehicle_type'] for v in vehicle_types])
        context['vehicles_by_type_data'] = json.dumps([v['count'] for v in vehicle_types])

        # Incidents by severity
        incident_severities = Incident.objects.values('severity').annotate(count=Count('id'))
        context['incidents_by_severity_labels'] = json.dumps([i['severity'] for i in incident_severities])
        context['incidents_by_severity_data'] = json.dumps([i['count'] for i in incident_severities])

        # Parking occupancy
        context['parkings'] = Parking.objects.all()

        # Recent vehicles
        context['recent_vehicles'] = Vehicle.objects.order_by('-id')[:5]

        return context
