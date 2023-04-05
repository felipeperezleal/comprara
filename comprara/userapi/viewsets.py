from rest_framework import viewsets
from . import models
from . import serializers

class ClienteViewset(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer

#List(), read(), create(), update(), destroy()
