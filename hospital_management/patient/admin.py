from django.contrib import admin
from patient.models import Patient
# Register your models here.
class patientAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'disease_category', 'dob', 'date_admitted')
    list_filter = ('date_admitted', 'disease_category', 'state')

admin.site.register(Patient, patientAdmin)