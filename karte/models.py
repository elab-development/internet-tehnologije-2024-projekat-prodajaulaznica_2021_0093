from django.db import models
from utakmice.models import Utakmica
from login.models import Korisnik

class TipKarte(models.Model):
    naziv = models.CharField(max_length=100)


class Karte(models.Model):
    tip_karte = models.ForeignKey(TipKarte, on_delete=models.CASCADE)
    kupac = models.ForeignKey(Korisnik, on_delete = models.RESTRICT)
    cena = models.DecimalField(max_digits=6, decimal_places=2)


class PreostaloKarata(models.Model):
    utakmica = models.ForeignKey(Utakmica, on_delete = models.CASCADE)
    tip_karte = models.ForeignKey(TipKarte, on_delete=models.CASCADE)
    preostalo = models.PositiveIntegerField()