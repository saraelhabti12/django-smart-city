from django.urls import path
from .views import DashboardView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', DashboardView.as_view(), name='dashboard'),
]