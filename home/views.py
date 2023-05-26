from django.http import HttpResponseRedirect
from django.shortcuts import render
import mercadopago

# Create your views here.
def index(request):
    return render(request, 'index.html')

def complete_donation(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        
        sdk = mercadopago.SDK("TEST-6696691551497362-052611-43405d44586a0bb3b75cb54e4db9c195-1383063111")    
        # Crea un ítem en la preferencia
        preference_data = {
            "items": [
                {
                    "title": "Comprara! apoyo económico",
                    "quantity": 1,
                    "unit_price": int(amount)
                }
            ]
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response['response']['init_point']
        return HttpResponseRedirect(preference)
    
    return render(request, 'donate.html')
