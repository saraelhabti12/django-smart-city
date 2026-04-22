from django.urls import path
from .views import (
    RoadListView, RoadDetailView, RoadCreateView, 
    RoadUpdateView, RoadDeleteView
)

urlpatterns = [
    path('', RoadListView.as_view(), name='road-list'),
    path('new/', RoadCreateView.as_view(), name='road-create'),
    path('<int:pk>/', RoadDetailView.as_view(), name='road-detail'),
    path('<int:pk>/edit/', RoadUpdateView.as_view(), name='road-update'),
    path('<int:pk>/delete/', RoadDeleteView.as_view(), name='road-delete'),
]