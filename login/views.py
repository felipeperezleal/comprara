from django.shortcuts import render, redirect
from django.contrib import messages
# Importamos el modelo de usuario que ya viene con Django
from django.contrib.auth.models import User
# Importamos autenticación, login y logout de Django
from django.contrib.auth import authenticate, login, logout

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Si el usuario existe en la base de datos, login
        try:
            user = User.objects.get(email=email)
            return render(request, 'login.html', {'user_email':email})
        # Si no está, error
        except:
            messages.error(request, 'Este correo no está registrado')

def register(request):
    return render(request, 'register.html')

def complete_registration(request):
    if request.POST.get('password') == request.POST.get('passwordConfirm'):
        user = User(email=request.POST['email'], password=request.POST['password'])
        user.save()
        return redirect('../../login/')
    else:
        messages.error(request, 'Las contraseñas no coinciden')
        return render(request, 'register.html')