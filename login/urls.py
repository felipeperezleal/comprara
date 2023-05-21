from django.urls import path
from . import views
from home.views import index, donate
from user.views import profile

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('register/', views.register, name="register"),
    path('register/complete/', views.complete_registration, name="complete_registration"),
    path('login/complete/', views.complete_login, name="complete_login"),
    path('search/', views.search, name="search"),
    path('filter/', views.filter, name="filter"),
    path('sort_ascending/', views.sort_ascending, name="sort_ascending"),
    path('sort_descending/', views.sort_descending, name="sort_descending"),
    path('profile/', profile, name="profile"),
    path('donate/', donate, name="donate"),
    path('', index, name="home"),
]