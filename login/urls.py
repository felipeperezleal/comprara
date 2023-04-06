from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('register/complete/', views.complete_registration, name="complete_registration"),
]