from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('donation/', views.complete_donation, name='complete_donation')
]