from django.shortcuts import render

from utakmice.models import Utakmica

# Create your views here.
def pocetna(zahtev):
    tekme = Utakmica.objects.all()
    return render(zahtev,'index.html',{'tekme':tekme})