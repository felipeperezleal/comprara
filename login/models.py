from django.db import models

# Create your models here.
class Client(models.Model):
    username = models.CharField(max_length=12)
    email = models.EmailField(max_length=64)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=16)