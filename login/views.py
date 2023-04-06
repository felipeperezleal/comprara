from django.shortcuts import render, redirect
from .models import Client

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def complete_registration(request):
    user = Client(email=request.POST['email'], password=request.POST['password'])
    user.save()
    return redirect('../../login/')