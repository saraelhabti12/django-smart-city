from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from roads.models import Road
from .models import Incident
from .forms import IncidentForm

class IncidentListView(LoginRequiredMixin, ListView):
    model = Incident
    template_name = 'incidents/incident_list.html'
    context_object_name = 'incidents'
    
    def get_queryset(self):
        queryset = Incident.objects.select_related('road').all()
        
        search_query = self.request.GET.get('search', '')
        severity = self.request.GET.get('severity', '')
        status = self.request.GET.get('status', '')
        road_id = self.request.GET.get('road', '')
        date = self.request.GET.get('date', '')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
            
        if severity:
            queryset = queryset.filter(severity=severity)
            
        if status:
            queryset = queryset.filter(status=status)
            
        if road_id:
            queryset = queryset.filter(road_id=road_id)
            
        if date:
            queryset = queryset.filter(created_at__date=date)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incident_severities'] = Incident.SEVERITY_CHOICES
        context['incident_statuses'] = Incident.STATUS_CHOICES
        context['roads'] = Road.objects.all()
        return context

class IncidentDetailView(LoginRequiredMixin, DetailView):
    model = Incident
    template_name = 'incidents/incident_detail.html'
    context_object_name = 'incident'

class IncidentCreateView(LoginRequiredMixin, CreateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incidents/incident_form.html'
    success_url = reverse_lazy('incident-list')

class IncidentUpdateView(LoginRequiredMixin, UpdateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incidents/incident_form.html'
    success_url = reverse_lazy('incident-list')

class IncidentDeleteView(LoginRequiredMixin, DeleteView):
    model = Incident
    template_name = 'incidents/incident_confirm_delete.html'
    success_url = reverse_lazy('incident-list')