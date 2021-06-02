from django.urls import path
from panel.views import DashboardView, PatientOp, PatientView, PatientDetails, PatientEdit, deletePatient, searchData
from django_filters.views import FilterView
from patient.filters import PatientFilter
urlpatterns = [
    path('', DashboardView.as_view(), name="Dashboard"),
    path('dashboard.view/', DashboardView.as_view(), name="Dashboard"),
    path('patient.add/', PatientOp.as_view(), name="PatientView"),
    path('patient/list.view/', PatientView.as_view(), name="PatientView"),
    path('patient/<patient_id>/detail.view/', PatientDetails.as_view(), name="PatientDetails"),
    path('patient/<id>/edit.view/', PatientEdit.as_view(), name="PatientEdit"),
    path('patient/<id>/delete.do/', deletePatient, name="PatientDelete"),
    path('patient/search/', searchData, name="searchData"),
    
]