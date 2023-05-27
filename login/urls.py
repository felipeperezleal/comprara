from django.urls import path
from . import views
from home.views import index, complete_donation
from user.views import profile, change_password, remove_product

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('login/reset-password/', views.reset_password, name="reset_password"),
    path('login/reset-password/email-sent/', views.send_email, name="send_email"),
    path('login/reset-password/new-password/', views.new_password, name="new_password"),
    path('logout/', views.logout_request, name="logout"),
    path('register/', views.register, name="register"),
    path('terms-conditions/', views.termsandconditions, name="termsandconditions"),
    path('register/complete/', views.complete_registration, name="complete_registration"),
    path('login/complete/', views.complete_login, name="complete_login"),
    path('search/', views.search, name="search"),
    path('filter/', views.filter, name="filter"),
    path('save-product/', views.save_product, name="save_product"),
    path('sort-ascending/', views.sort_ascending, name="sort_ascending"),
    path('sort-descending/', views.sort_descending, name="sort_descending"),
    path('by-seller/', views.byseller, name="byseller"),
    path('clear/', views.clear_filter, name="clear_filter"),
    path('profile/change-password/', change_password, name="change_password"),
    path('profile/remove-product/', remove_product, name="remove_product"),
    path('profile/', profile, name="profile"),
    path('donate/', complete_donation, name="donate"),
    path('', index, name="home"),
]