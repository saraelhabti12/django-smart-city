from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Road
from .forms import RoadForm

class RoadListView(LoginRequiredMixin, ListView):
    model = Road
    template_name = 'roads/road_list.html'
    context_object_name = 'roads'

class RoadDetailView(LoginRequiredMixin, DetailView):
    model = Road
    template_name = 'roads/road_detail.html'
    context_object_name = 'road'

class RoadCreateView(LoginRequiredMixin, CreateView):
    model = Road
    form_class = RoadForm
    template_name = 'roads/road_form.html'
    success_url = reverse_lazy('road-list')

class RoadUpdateView(LoginRequiredMixin, UpdateView):
    model = Road
    form_class = RoadForm
    template_name = 'roads/road_form.html'
    success_url = reverse_lazy('road-list')

class RoadDeleteView(LoginRequiredMixin, DeleteView):
    model = Road
    template_name = 'roads/road_confirm_delete.html'
    success_url = reverse_lazy('road-list')