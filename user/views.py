from django.shortcuts import render
import requests

# Create your views here.
def profile(request):
    return render(request, 'profile.html')