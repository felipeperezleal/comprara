from django.shortcuts import render, redirect
from django.contrib import messages
# Importamos el modelo de usuario que ya viene con Django
from django.contrib.auth.models import User
from .models import Product
# Importamos autenticación, login y logout de Django
from django.contrib.auth import authenticate, login, logout
from bs4 import BeautifulSoup as bs
import requests, json, random

def search(request):
    search_string = request.POST.get('search_string').replace(' ', '%20')
    products = []
    try:
        products.extend(exito_sc(search_string))
    except:
        pass
    try:
        products.extend(metro_sc(search_string))
    except:
        pass
    try:
        products.extend(jumbo_sc(search_string))
    except:
        pass
    try:
        products.extend(olimpica_sc(search_string))
    except:
        pass

    random.shuffle(products)
    return render(request, 'search.html', {'products':products})

def save_product(request):
    '''
    url = request.POST.get('product_url')
    '''
    user = User.objects.filter(id=request.user.id)
    print(user)

    # product = Product(url, user.id)

def metro_sc(query):
    url = f'https://www.tiendasmetro.co/{query}?_q={query}&map=ft'
    #Replace User-Agent header (this protects Scraping by getting banned from the website)
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"})
    soup = bs(r.content, 'html.parser')
    script = soup.findAll('script', {'type':'application/ld+json'})
    data = json.loads(script[2].text)
    products = []
    print(data)
    for product in data['itemListElement']:
        products.append([product['item']['name'], product['item']['offers']['lowPrice'], product['item']['image'], product['item']['@id'], "Metro"])
    return products

def exito_sc(query):
    url = f'https://www.exito.com/{query}?_q={query}&map=ft'
    #Replace User-Agent header (this protects Scraping by getting banned from the website)
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"})
    soup = bs(r.content, 'html.parser')
    script = soup.findAll('script', {'type':'application/ld+json'})
    data = json.loads(script[2].text)
    products = []
    for product in data['itemListElement']:
        products.append([product['item']['name'], product['item']['offers']['lowPrice'], product['item']['image'], product['item']['@id'], "Éxito"])
    return products

def jumbo_sc(query):
    url = f'https://www.tiendasjumbo.co/{query}?_q={query}&map=ft'
    #Replace User-Agent header (this protects Scraping by getting banned from the website)
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"})
    soup = bs(r.content, 'html.parser')
    script = soup.findAll('script', {'type':'application/ld+json'})
    data = json.loads(script[2].text)
    products = []
    for product in data['itemListElement']:
        products.append([product['item']['name'], product['item']['offers']['lowPrice'], product['item']['image'], product['item']['@id'], "Jumbo"])
    return products

def olimpica_sc(query):
    url = f'https://www.olimpica.com/{query}?_q={query}&map=ft'
    #Replace User-Agent header (this protects Scraping by getting banned from the website)
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"})
    soup = bs(r.content, 'html.parser')
    script = soup.findAll('script', {'type':'application/ld+json'})
    data = json.loads(script[2].text)
    products = []
    for product in data['itemListElement']:
        products.append([product['item']['name'], product['item']['offers']['lowPrice'], product['item']['image'], product['item']['@id'], "Olímpica"])
    return products

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
        return redirect('login')
    else:
        messages.error(request, 'Las contraseñas no coinciden')
        return render(request, 'register.html')

def logout_request(request):
    logout(request)    
    return redirect('../../')
