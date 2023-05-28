from rest_framework.routers import DefaultRouter
from login.api.views import UserApiViewSet

router_user = DefaultRouter()

router_user.register(prefix='users', viewset=UserApiViewSet, basename='users')