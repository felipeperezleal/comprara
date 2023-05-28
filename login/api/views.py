from rest_framework.viewsets import ModelViewSet
from login.models import CustomUser
from login.api.serializers import CustomUserSerializer

class UserApiViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
