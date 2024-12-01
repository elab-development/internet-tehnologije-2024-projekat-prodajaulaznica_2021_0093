# utakmice/models.py
from django.db import models

class Utakmica(models.Model):
    naziv = models.CharField(max_length=100)
    datum = models.DateTimeField()
    lokacija = models.CharField(max_length=100)
    broj_mesta = models.PositiveIntegerField()
    ostalo_mesta = models.PositiveIntegerField()

    def __str__(self):
        return self.naziv

class TipKarte(models.Model):
    naziv = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.naziv

