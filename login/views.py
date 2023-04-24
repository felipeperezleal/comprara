from django.shortcuts import render, redirect
from django.contrib import messages
# Importamos el modelo de usuario que ya viene con Django
from django.contrib.auth.models import User
# Importamos autenticación, login y logout de Django
from django.contrib.auth import authenticate, login, logout
from bs4 import BeautifulSoup as bs
import requests

def search(request):
    search_string = request.POST.get('search_string')
    url = 'https://listado.mercadolibre.com.co/' + search_string.replace(' ', '-')
    r = requests.get(url)
    soup = bs(r.content)
    item_titles = soup.find_all('h2', {'class':"ui-search-item__title shops__item-title"})

    # Debug, imprime en consola los títulos de los artículos que son resultado de la búsqueda
    for title in item_titles:
        print(title)
    
    return render(request, 'search.html')


def login_view(request):
    return render(request, 'login.html')

def complete_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Si el usuario existe en la base de datos, login
        try:
            user = User.objects.get(username=username)
        # Si no está, error
        except:
            messages.error(request, 'Este usuario no existe')
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)

        # Si ha sido autenticado, log in. De lo contrario, error
        if user is not None:
            login(request, user)
            return redirect('../../')
        else:
            messages.error(request, 'Usuario o contraseña erróneos')
            return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def complete_registration(request):
    if request.POST.get('password') == request.POST.get('passwordConfirm'):
        user = User(username = request.POST['username'], password = request.POST['password'])
        user.set_password(request.POST['password'])
        user.save()
        return redirect('home')
    else:
        messages.error(request, 'Las contraseñas no coinciden')
        return render(request, 'register.html')

def logout_request(request):
    logout(request)    
    return redirect('../../')
