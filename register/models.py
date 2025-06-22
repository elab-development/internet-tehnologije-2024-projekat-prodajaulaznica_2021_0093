from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    broj_kartice = models.CharField(max_length=30)
