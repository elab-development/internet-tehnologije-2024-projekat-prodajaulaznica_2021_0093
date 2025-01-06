from django.db import models
from utakmice.models import Utakmica
from django.contrib.auth.models import User

class TipKarte(models.Model):
    naziv = models.CharField(max_length=100)
    def __str__(self):
        return self.naziv


class Karte(models.Model):
    tip_karte = models.ForeignKey(TipKarte, on_delete=models.RESTRICT)
    kupac = models.ForeignKey(User, on_delete = models.RESTRICT)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    utakmica = models.ForeignKey(Utakmica, on_delete=models.RESTRICT, default=1)


class PreostaloKarata(models.Model):
    utakmica = models.ForeignKey(Utakmica, on_delete = models.RESTRICT)
    tip_karte = models.ForeignKey(TipKarte, on_delete=models.RESTRICT)
    preostalo = models.PositiveIntegerField()