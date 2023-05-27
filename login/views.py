from email.message import EmailMessage
import smtplib
import uuid
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
# Importamos el modelo de usuario que ya viene con Django
from .models import CustomUser as User
# Importamos autenticación, login y logout de Django
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from bs4 import BeautifulSoup as bs
import requests, json, random

def search(request):
    search_string = request.POST.get('search_string').replace(' ', '%20')
    global list_products
    list_products = []
    try:
        list_products.extend(exito_sc(search_string))
    except:
        pass
    try:
        list_products.extend(metro_sc(search_string))
    except:
        pass
    try:
        list_products.extend(jumbo_sc(search_string))
    except:
        pass
    try:
        list_products.extend(olimpica_sc(search_string))
    except:
        pass

    random.shuffle(list_products)

    return render(request, 'search.html', {'products':list_products})

def metro_sc(query):
    url = f'https://www.tiendasmetro.co/{query}?_q={query}&map=ft'
    #Replace User-Agent header (this protects Scraping by getting banned from the website)
    user_agent_list = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15', 
    ]
    for i in range(1,4):
        user_agent = random.choice(user_agent_list)
        
    r = requests.get(url, headers={"User-Agent": user_agent})
    soup = bs(r.content, 'html.parser')
    script = soup.findAll('script', {'type':'application/ld+json'})
    data = json.loads(script[2].text)
    products = []
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
            return render(request, 'login.html')
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)

        # Si ha sido autenticado, log in. De lo contrario, error
        if user is not None:
            login(request, user)
            return redirect('../../')
        else:
            messages.error(request, 'Contraseña incorrecta')
            return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def termsandconditions(request):
    return render(request, 'terms.html')

def complete_registration(request):
    if request.POST.get('password') == request.POST.get('passwordConfirm'):
        user = User(username = request.POST['username'], password = request.POST['password'], inventory = [])
        user.set_password(request.POST['password'])
        user.save()
        return redirect('login')
    else:
        messages.error(request, 'Las contraseñas no coinciden')
        return render(request, 'register.html')

def logout_request(request):
    logout(request)    
    return redirect('../../')

def filter(request):
    try:
        fproducts = list_products
    except:
        fproducts = []
    min_price = request.POST.get('min_price')
    max_price = request.POST.get('max_price')
    fproducts = [product for product in fproducts if int(product[1]) >= int(min_price) and int(product[1]) <= int(max_price)]
    
    return render(request, 'search.html', {'products':fproducts})

def clear_filter(request):
    try:
        fproducts = list_products
    except:
        fproducts = []
    return render(request, 'search.html', {'products':fproducts})

def sort_ascending(request):
    try:
        sproducts = list_products
    except:
        sproducts = []
    sort = request.POST.get('sort')
    sproducts = sorted(sproducts, key=lambda x: x[1])

    return render(request, 'search.html', {'products':sproducts})

def sort_descending(request):
    try:
        sproducts = list_products
    except:
        sproducts = []
    sort = request.POST.get('sort')
    sproducts = sorted(sproducts, key=lambda x: x[1], reverse=True)

    return render(request, 'search.html', {'products':sproducts})

def byseller(request):
    try:
        fproducts = list_products
    except:
        fproducts = []
    filterbys = []

    if request.method == 'POST':
        if 'exito' in request.POST:
            try:
                filterbys += [product for product in fproducts if product[-1] == "Éxito"]
            except:
                pass
        if 'metro' in request.POST:
            try:
                filterbys += [product for product in fproducts if product[-1] == "Metro"]
            except:
                pass
        if 'jumbo' in request.POST:
            try:
                filterbys += [product for product in fproducts if product[-1] == "Jumbo"]
            except:
                pass
        if 'olimpica' in request.POST:
            try:
                filterbys += [product for product in fproducts if product[-1] == "Olímpica"]
            except:
                pass
    
    return render(request, 'search.html', {'products':filterbys})

def save_product(request):
    if request.method == 'POST':
        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        image = request.POST.get('product_image')
        url = request.POST.get('product_store')
        seller = request.POST.get('product_seller')
        user = request.user
        user.inventory.append([name, price, image, url, seller])
        user.save()
    lproducts = list_products
    return render(request, 'search.html', {'products':lproducts})

def reset_password(request):
    return render(request, './reset_password/reset_password.html')

def send_email(request):
    admin = "compraraunal@outlook.com"
    global receiver
    receiver = request.POST.get('username')
    email = EmailMessage()
    email["From"] = admin
    email["To"] = receiver
    email["Subject"] = "Comprara! | Recuperar contraseña"
    reset_link = request.build_absolute_uri(f"../new-password")
    email.set_content("Haz click en el siguiente enlace para recuperar tu contraseña: " + reset_link)
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(admin, "Comprara2023")
    smtp.sendmail(admin, receiver, email.as_string())
    smtp.quit()
    return render(request, './reset_password/email_sent.html')

def new_password(request):
    try:
        if request.method == 'POST':
            pswd1 = request.POST.get('pswd1')
            pswd2 = request.POST.get('pswd2')
            if pswd1 == pswd2:
                user = User.objects.get(username=receiver)
                user.set_password(pswd1)
                user.save()
                messages.success(request, 'Contraseña actualizada')
                return redirect('login')
            else:
                messages.error(request, 'Las contraseñas no coinciden')
    except:
        pass

    return render(request, './reset_password/new_password.html')