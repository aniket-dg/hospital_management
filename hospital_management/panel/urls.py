from django.urls import path
from panel.views import DashboardView, PatientOp, PatientView, PatientDetails, PatientEdit, deletePatient, searchData

from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(DashboardView.as_view()), name="Dashboard"),
    path('dashboard.view/', login_required(DashboardView.as_view()), name="Dashboard"),
    path('patient.add/', login_required(PatientOp.as_view()), name="PatientView"),
    path('patient/list.view/', login_required(PatientView.as_view()), name="PatientView"),
    path('patient/<patient_id>/detail.view/', login_required(PatientDetails.as_view()), name="PatientDetails"),
    path('patient/<id>/edit.view/', login_required(PatientEdit.as_view()), name="PatientEdit"),
    path('patient/<id>/delete.do/', deletePatient, name="PatientDelete"),
    path('patient/search/', searchData, name="searchData"),
        
]
