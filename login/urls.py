from django.urls import path
from . import views
from home.views import index

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('register/', views.register, name="register"),
    path('register/complete/', views.complete_registration, name="complete_registration"),
    path('login/complete/', views.complete_login, name="complete_login"),
    path('', index, name="home"),
]