from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('profile/change-password', views.change_password, name="change_password"),
]