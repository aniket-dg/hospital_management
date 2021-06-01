from django.shortcuts import render
from django.views import View
# Create your views here.
class DashboardView(View):
    template_name = 'panel/index.html'
    def get(self, request):
        return render(request, self.template_name)

class PatientOp(View):
    template_name = 'panel/addPatient.html'
    def get(self, request):
        return render(request, self.template_name)
