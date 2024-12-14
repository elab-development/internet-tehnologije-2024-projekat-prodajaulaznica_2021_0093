from django.db import models


class Korisnik(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    brojKartice = models.CharField(max_length=20)

