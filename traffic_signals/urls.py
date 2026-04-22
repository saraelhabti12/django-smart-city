from django.urls import path
from .views import (
    TrafficSignalListView, TrafficSignalDetailView, TrafficSignalCreateView,
    TrafficSignalUpdateView, TrafficSignalDeleteView
)

urlpatterns = [
    path('', TrafficSignalListView.as_view(), name='signal-list'),
    path('new/', TrafficSignalCreateView.as_view(), name='signal-create'),
    path('<int:pk>/', TrafficSignalDetailView.as_view(), name='signal-detail'),
    path('<int:pk>/edit/', TrafficSignalUpdateView.as_view(), name='signal-update'),
    path('<int:pk>/delete/', TrafficSignalDeleteView.as_view(), name='signal-delete'),
]