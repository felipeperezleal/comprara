from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    user = models.CharField(max_length=10)
    password = models.CharField(max_length=16)

    #Create - POST
    #Read   - GET
    #Update - PUT
    #Delete - DELTE
