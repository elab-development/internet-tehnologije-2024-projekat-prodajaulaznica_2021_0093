# utakmice/models.py
from django.db import models

class Utakmica(models.Model):
    protivnik = models.CharField(max_length=100)
    datumVreme = models.DateTimeField()
    lokacija = models.CharField(max_length=100)    
    urlSlike = models.CharField(max_length=2086, blank=True, null=True)

    def __str__(self):
        return f'Partizan VS {self.protivnik} - {self.datumVreme.date()}'

