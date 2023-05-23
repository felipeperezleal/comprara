from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inventory = ArrayField(ArrayField(models.CharField(max_length=50)), blank=True, null=True)

    def __str__(self):
        return self.user.username