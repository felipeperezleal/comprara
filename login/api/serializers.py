from rest_framework.serializers import ModelSerializer
from login.models import CustomUser
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'date_joined', 'last_login') 