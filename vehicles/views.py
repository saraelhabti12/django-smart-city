from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from roads.models import Road
from .models import Vehicle, PriorityVehicle
from .forms import VehicleForm, PriorityVehicleForm

class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_list.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        search_query = self.request.GET.get('search', '')
        vehicle_type = self.request.GET.get('type', '')
        status = self.request.GET.get('status', '')
        road_id = self.request.GET.get('road', '')
        battery_level = self.request.GET.get('battery', '')

        if search_query:
            queryset = queryset.filter(
                Q(plate_number__icontains=search_query) |
                Q(destination__icontains=search_query)
            )
            
        if vehicle_type:
            queryset = queryset.filter(vehicle_type=vehicle_type)
            
        if status:
            queryset = queryset.filter(status=status)
            
        if road_id:
            queryset = queryset.filter(current_road_id=road_id)
            
        if battery_level:
            if battery_level == 'low':
                queryset = queryset.filter(battery_level__lt=20)
            elif battery_level == 'medium':
                queryset = queryset.filter(battery_level__gte=20, battery_level__lt=50)
            elif battery_level == 'high':
                queryset = queryset.filter(battery_level__gte=50)
                
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle_types'] = Vehicle.TYPE_CHOICES
        context['vehicle_statuses'] = Vehicle.STATUS_CHOICES
        context['roads'] = Road.objects.all()
        return context

class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'vehicles/vehicle_detail.html'
    context_object_name = 'vehicle'

class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicle-list')

class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicle-list')

class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicles/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle-list')

class PriorityVehicleListView(LoginRequiredMixin, ListView):
    model = PriorityVehicle
    template_name = 'vehicles/priority_list.html'
    context_object_name = 'priority_vehicles'

    def get_queryset(self):
        return PriorityVehicle.objects.select_related('vehicle').all()

class PriorityVehicleDetailView(LoginRequiredMixin, DetailView):
    model = PriorityVehicle
    template_name = 'vehicles/priority_detail.html'
    context_object_name = 'priority_vehicle'

class PriorityVehicleCreateView(LoginRequiredMixin, CreateView):
    model = PriorityVehicle
    form_class = PriorityVehicleForm
    template_name = 'vehicles/priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityVehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = PriorityVehicle
    form_class = PriorityVehicleForm
    template_name = 'vehicles/priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityVehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = PriorityVehicle
    template_name = 'vehicles/priority_confirm_delete.html'
    success_url = reverse_lazy('priority-list')