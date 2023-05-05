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

    product_titles = soup.findAll('h2', {'class':"ui-search-item__title shops__item-title"})
    product_images = soup.findAll('img', {'class':"ui-search-result-image__element shops__image-element"})
    product_prices = soup.findAll('span', {'class':"price-tag-fraction"})
        
    products = []
    i = 0
    for title in product_titles:
        products.append([product_titles[i].text, product_prices[i].text])
        i = i + 1

    return render(request, 'search.html', {'products':products})

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
