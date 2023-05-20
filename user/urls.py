from django.urls import path
from . import views
from home.views import index

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('', index, name="home"),
]