from django.urls import path
from .views import (
    IncidentListView, IncidentDetailView, IncidentCreateView, 
    IncidentUpdateView, IncidentDeleteView
)

urlpatterns = [
    path('', IncidentListView.as_view(), name='incident-list'),
    path('new/', IncidentCreateView.as_view(), name='incident-create'),
    path('<int:pk>/', IncidentDetailView.as_view(), name='incident-detail'),
    path('<int:pk>/edit/', IncidentUpdateView.as_view(), name='incident-update'),
    path('<int:pk>/delete/', IncidentDeleteView.as_view(), name='incident-delete'),
]