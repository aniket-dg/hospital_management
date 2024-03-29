from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
class MyLoginView(View):
    template_name = 'authentication/index.html'

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        email = request.POST['email_address']
        password = request.POST['password']
        user = authenticate(request, username = email, password = password)
        if user is not None:
            login(request, user)
            return redirect('/panel/dashboard.view')
        else:
            messages.warning(request, "Invalid Login Credentials")
            return redirect('/accounts/')

def logoutUser(request):
    logout(request)
    return redirect('/accounts/') 
        