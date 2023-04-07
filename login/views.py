from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Client

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def complete_registration(request):
    if request.POST.get('password') == request.POST.get('passwordConfirm'):
        user = Client(email=request.POST['email'], password=request.POST['password'])
        user.save()
        return redirect('../../login/')
    else:
        messages.error(request, 'Las contraseñas no coinciden')
        return render(request, 'register.html')