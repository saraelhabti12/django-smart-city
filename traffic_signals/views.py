from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TrafficSignal
from .forms import TrafficSignalForm

class TrafficSignalListView(LoginRequiredMixin, ListView):
    model = TrafficSignal
    template_name = 'traffic_signals/signal_list.html'
    context_object_name = 'signals'
    
    def get_queryset(self):
        return TrafficSignal.objects.select_related('intersection').all()

class TrafficSignalDetailView(LoginRequiredMixin, DetailView):
    model = TrafficSignal
    template_name = 'traffic_signals/signal_detail.html'
    context_object_name = 'signal'

class TrafficSignalCreateView(LoginRequiredMixin, CreateView):
    model = TrafficSignal
    form_class = TrafficSignalForm
    template_name = 'traffic_signals/signal_form.html'
    success_url = reverse_lazy('signal-list')

class TrafficSignalUpdateView(LoginRequiredMixin, UpdateView):
    model = TrafficSignal
    form_class = TrafficSignalForm
    template_name = 'traffic_signals/signal_form.html'
    success_url = reverse_lazy('signal-list')

class TrafficSignalDeleteView(LoginRequiredMixin, DeleteView):
    model = TrafficSignal
    template_name = 'traffic_signals/signal_confirm_delete.html'
    success_url = reverse_lazy('signal-list')