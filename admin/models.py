from django.db import models
from korisnici.models import Korisnik

class Admin(models.Model):
    korisnik = models.OneToOneField(Korisnik, on_delete=models.CASCADE)
    privilegije = models.CharField(max_length=100)

    def __str__(self):
        return self.korisnik.username
