from django.db import models
from utakmice.models import Utakmica

class TipKarte(models.Model):
    naziv = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.naziv

class Karte(models.Model):
    utakmica = models.ForeignKey(Utakmica, on_delete=models.CASCADE)
    tip_karte = models.ForeignKey(TipKarte, on_delete=models.CASCADE)
    broj_karata = models.PositiveIntegerField()
    raspolozivo = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tip_karte.naziv} karte za utakmicu {self.utakmica.naziv}"
    