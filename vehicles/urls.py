from django.urls import path
from .views import (
    VehicleListView, VehicleDetailView, VehicleCreateView, 
    VehicleUpdateView, VehicleDeleteView,
    PriorityVehicleListView, PriorityVehicleDetailView, PriorityVehicleCreateView,
    PriorityVehicleUpdateView, PriorityVehicleDeleteView
)

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle-list'),
    path('new/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('<int:pk>/edit/', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle-delete'),
    
    path('priority/', PriorityVehicleListView.as_view(), name='priority-list'),
    path('priority/new/', PriorityVehicleCreateView.as_view(), name='priority-create'),
    path('priority/<int:pk>/', PriorityVehicleDetailView.as_view(), name='priority-detail'),
    path('priority/<int:pk>/edit/', PriorityVehicleUpdateView.as_view(), name='priority-update'),
    path('priority/<int:pk>/delete/', PriorityVehicleDeleteView.as_view(), name='priority-delete'),
]