from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Parking
from .forms import ParkingForm

class ParkingListView(LoginRequiredMixin, ListView):
    model = Parking
    template_name = 'parking/parking_list.html'
    context_object_name = 'parkings'

class ParkingDetailView(LoginRequiredMixin, DetailView):
    model = Parking
    template_name = 'parking/parking_detail.html'
    context_object_name = 'parking'

class ParkingCreateView(LoginRequiredMixin, CreateView):
    model = Parking
    form_class = ParkingForm
    template_name = 'parking/parking_form.html'
    success_url = reverse_lazy('parking-list')

class ParkingUpdateView(LoginRequiredMixin, UpdateView):
    model = Parking
    form_class = ParkingForm
    template_name = 'parking/parking_form.html'
    success_url = reverse_lazy('parking-list')

class ParkingDeleteView(LoginRequiredMixin, DeleteView):
    model = Parking
    template_name = 'parking/parking_confirm_delete.html'
    success_url = reverse_lazy('parking-list')