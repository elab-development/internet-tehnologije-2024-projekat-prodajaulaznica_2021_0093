# utakmice/models.py
from django.db import models

class Utakmica(models.Model):
    protivnik = models.CharField(max_length=100)
    datumVreme = models.DateTimeField()
    lokacija = models.CharField(max_length=100)



