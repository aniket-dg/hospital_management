from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from patient.models import Patient
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from patient.filters import PatientFilter
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
class DashboardView(View):
    template_name = 'panel/index.html'
    def get(self, request):
        return render(request, self.template_name)

class PatientOp(View):
    template_name = 'panel/addPatient.html'
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        patient_name = request.POST['patient_name']
        try:
            patient = Patient.objects.get(patient_name = patient_name)
            messages.warning(request, "Patient already existed in Database, Please edit existing data....")
            return redirect('/panel/patient/list.view/')
        except ObjectDoesNotExist:
            patient = Patient(patient_name = patient_name, contact_no = request.POST['contact_no'],
            email = request.POST['email_address'], state = request.POST['state'], 
            street_address = request.POST['street_address'], house_no = request.POST['house_no'],
            city = request.POST['city'], zip = request.POST['zip_code'], dob = request.POST['dob'],
            gender = request.POST['gender'], maritual_status = request.POST['maritual_status'],
            disease_category = request.POST['disease_category'], problem = request.POST['problem'],
            previous_health_issue = request.POST['previous_health_issue']
            )
            patient.save()
            messages.success(request, "Patient data added successfully")
            return redirect('/panel/patient/list.view/')


class PatientView(ListView):
    model = Patient
    template_name = 'panel/listPatient.html'
    def get(self, request):
        context = {}
        patients = Patient.objects.all()
        paginator = Paginator(patients, 2)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        if page.has_next():
            next_url = f'?page={page.next_page_number()}'
        else:
            next_url = ''
        
        if page.has_previous():
            prev_url = f'?page={page.previous_page_number()}'
        else:
            prev_url = ''
        context['patients'] = page
        context['next_url'] = next_url
        context['prev_url'] = prev_url
        return render(request, self.template_name, context=context)


class PatientDetails(View):
    template_name = 'panel/patientDetails.html'
    model = Patient
    def get(self, request, patient_id):
        try:
            patient = Patient.objects.get(id = patient_id)
            return render(request, self.template_name, { 'patient': patient }) 
        except ObjectDoesNotExist:
            messages.warning(request, "Sorry, patient not Found!")
            return render(request, self.template_name)

class PatientEdit(View):
    template_name = 'panel/editPatient.html'
    def get(self,request, id):
        try:
            patient = Patient.objects.get(id = id)
            return render(request, self.template_name, { 'patient': patient }) 
        except ObjectDoesNotExist:
            messages.warning(request, "Sorry, patient not Found!")
            return render(request, self.template_name)

    def post(self, request, id):
        patient = Patient.objects.filter(id = id).update(patient_name = request.POST['patient_name'], contact_no = request.POST['contact_no'],
            email = request.POST['email_address'], state = request.POST['state'], 
            street_address = request.POST['street_address'], house_no = request.POST['house_no'],
            city = request.POST['city'], zip = request.POST['zip_code'],
            gender = request.POST['gender'], maritual_status = request.POST['maritual_status'],
            disease_category = request.POST['disease_category'], problem = request.POST['problem'],
            previous_health_issue = request.POST['previous_health_issue']
            )
        messages.success(request, "Patient data edited successfully")
        str = "/panel/patient/{id}/detail.view/".format(id = id)
        return redirect(str)

def deletePatient(request, id):
    patient = Patient.objects.filter(id = id).delete()
    messages.warning(request, "Patient data deleted successfully")
    return redirect('/panel/patient/list.view/')


def searchData(request):
    if request.GET.get('q'):
       data = str(request.GET.get('q'))
       context = {}
       patient_filter = Patient.objects.filter(Q(patient_name__icontains = data) | Q(state__icontains = data) |
                                               Q(contact_no__icontains = data ) | Q(email__icontains = data ) |
                                               Q(disease_category__icontains = data ) | Q(zip__exact = data ) |
                                               Q(gender__iexact = data ) | Q(maritual_status__iexact = data )
        )
       context['patients'] = patient_filter
       return render(request, 'panel/listPatient.html', context=context)
    else:
        return redirect('/panel/patient/list.view/') 
    

        

