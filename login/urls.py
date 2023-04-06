from django.urls import path
from . import views
from home.views import index

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('register/complete/', views.complete_registration, name="complete_registration"),
    path('', index, name="home"),
]