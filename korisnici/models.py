from django.db import models
from django.contrib.auth.models import User

class Korisnik(models.Model):
    korisnik = models.OneToOneField(User, on_delete=models.CASCADE)
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.korisnik.username

