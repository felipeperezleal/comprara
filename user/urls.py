from django.urls import path
from . import views
from home.views import index

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('profile/complete/', views.change_password, name="complete"),
    path('', index, name="home"),
]