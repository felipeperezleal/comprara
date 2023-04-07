from django.shortcuts import render, redirect
from django.contrib import messages
# Importamos el modelo de usuario que ya viene con Django
from django.contrib.auth.models import User
# Importamos autenticación, login y logout de Django
from django.contrib.auth import authenticate, login, logout

def login(request):
    return render(request, 'login.html')

def complete_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Si el usuario existe en la base de datos, login
        try:
            user = User.objects.get(username=username)
        # Si no está, error
        except:
            messages.error(request, 'Este correo no está registrado')

        # Autenticar usuario
        user = authenticate(request, user=username, password=password)
        # Debug msg
        messages.info(request, 'Tried to authenticate with Username = {} Password: {}. user variable is {}'.format(username, password, user))

        # Si ha sido autenticado, log in. De lo contrario, error
        if user != None:
            login(request, user)
            # Debug msg
            messages.success(request, 'Login successful')
            return redirect('../../')
        else:
            messages.error(request, 'Email o contraseña erróneos')
            return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def complete_registration(request):
    if request.POST.get('password') == request.POST.get('passwordConfirm'):
        user = User(username = request.POST['email'], email=request.POST['email'], password=request.POST['password'])
        user.save()
        return redirect('../../login/')
    else:
        messages.error(request, 'Las contraseñas no coinciden')
        return render(request, 'register.html')