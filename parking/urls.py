from django.urls import path
from .views import (
    ParkingListView, ParkingDetailView, ParkingCreateView, 
    ParkingUpdateView, ParkingDeleteView
)

urlpatterns = [
    path('', ParkingListView.as_view(), name='parking-list'),
    path('new/', ParkingCreateView.as_view(), name='parking-create'),
    path('<int:pk>/', ParkingDetailView.as_view(), name='parking-detail'),
    path('<int:pk>/edit/', ParkingUpdateView.as_view(), name='parking-update'),
    path('<int:pk>/delete/', ParkingDeleteView.as_view(), name='parking-delete'),
]