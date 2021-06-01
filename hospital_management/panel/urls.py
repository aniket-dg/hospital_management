from django.urls import path
from panel.views import DashboardView, PatientOp
urlpatterns = [
    path('', DashboardView.as_view(), name="Dashboard"),
    path('dashboard.view/', DashboardView.as_view(), name="Dashboard"),
    path('patient.add/', PatientOp.as_view(), name="PatientView"),
]